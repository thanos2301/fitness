const { PrismaClient } = require('@prisma/client');
const express = require('express');
const cors = require("cors");
const bcrypt = require('bcrypt');
const validator = require('validator');
const jwt = require('jsonwebtoken');
const prisma = new PrismaClient();
const app = express();
app.use(express.json());
app.use(cors());
require('dotenv').config();

const saltRounds = 10; // Salt rounds for bcrypt
const secretKey = 'your-secret-key'; // Define your JWT secret key

// Example route to fetch all users (for debugging or display purposes)
app.get('/users', async (req, res) => {
  const users = await prisma.user.findMany();
  res.json(users);
});

// Route to sign up a new user
app.post('/signup', async (req, res) => {
  const { email, password } = req.body;

  // Email and password validation
  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password are required.' });
  }

  if (!validator.isEmail(email)) {
    return res.status(400).json({ error: 'Invalid email format.' });
  }

  if (password.length < 6) {
    return res.status(400).json({ error: 'Password must be at least 6 characters long.' });
  }

  try {
    // Check if the email is already registered
    const existingUser = await prisma.user.findUnique({
      where: { email: email }
    });

    if (existingUser) {
      return res.status(400).json({ error: 'Email already exists.' });
    }

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, saltRounds);

    // Create a new user
    const newUser = await prisma.user.create({
      data: {
        email: email,
        password: hashedPassword // Store the hashed password
      }
    });

    // Respond with the created user
    res.status(201).json({ message: 'User registered successfully', user: newUser });
  } catch (error) {
    console.error('Error signing up user:', error);
    res.status(500).json({ error: 'Error signing up user', details: error.message });
  }
});
// Route to sign in an existing user and generate a token
app.post('/signin', async (req, res) => {
  const { email, password } = req.body;

  try {
    // Find the user by email using Prisma
    const user = await prisma.user.findUnique({
      where: { email: email }
    });

    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    // Check if the password is valid
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    // Generate JWT token using the user's email and userId
    const token = jwt.sign({ email: user.email, userId: user.id }, secretKey, { expiresIn: '1h' });

    // Send the token back in the response
    res.status(200).json({ token, message: 'Signin successful' });

  } catch (error) {
    console.error('Error during signin:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});


// Middleware to verify JWT
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }

  try {
    const decodedToken = jwt.verify(token, secretKey);
    req.email = decodedToken.email; // Attach email to the request object
    req.userId = decodedToken.userId; // Attach userId to the request object
    next(); // Proceed to the next middleware or route
  } catch (err) {
    return res.status(403).json({ error: 'Invalid or expired token' });
  }
};


const axios = require("axios");

app.post('/home', authenticateToken, async (req, res) => {
  const { injury, age, gender } = req.body;
  const userId = req.userId; // Extract userId from token

  if (!userId) {
      return res.status(400).json({ error: "User ID not available in token" });
  }

  try {
      // Update the user's info (age, gender, injuries) based on userId
      const updatedUser = await prisma.user.update({
        where: { id: userId },
        data: {
          age: parseInt(age, 10), // Ensure age is an integer
          gender: gender,
          injuries: injury,
        },
      });
      

      console.log("User updated:", updatedUser);

      // Save the health data separately in HealthInfo
      

     

      // Send the data to the ML model API
      console.log("Sending request to ML model...");
      
     

    

      res.status(200).json({ message: "Prediction successful" });
  } catch (error) {
      console.error("Error processing request:", error);
      res.status(500).json({
          error: "Error processing request",
          details: error.message,
          stack: error.stack,
      });
  }
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
