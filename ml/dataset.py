import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load the dataset (make sure to update the file path)
dataset_path = 'C:/Users/thiya/OneDrive/Documents/pdlproject/ml/expanded_dataset.xlsx'  # Update this to the correct path
dataset = pd.read_excel(dataset_path)

# Step 2: Preprocess the data (convert categorical values to numerical)
le_gender = LabelEncoder()
dataset['gender'] = dataset['gender'].str.lower()  # Normalize gender input
dataset['gender'] = le_gender.fit_transform(dataset['gender'])

le_injuries = LabelEncoder()
dataset['injuries'] = dataset['injuries'].str.lower()  # Normalize injuries input
dataset['injuries'] = le_injuries.fit_transform(dataset['injuries'])

# Step 3: Split the dataset into features (X) and labels (y)
X = dataset[['age', 'gender', 'injuries']]
y_remedy = dataset['remedy']
y_exercise = dataset['exercise']

# Step 4: Train-Test split
X_train, X_test, y_remedy_train, y_remedy_test = train_test_split(X, y_remedy, test_size=0.2, random_state=42)
_, _, y_exercise_train, y_exercise_test = train_test_split(X, y_exercise, test_size=0.2, random_state=42)

# Step 5: Train the RandomForest models
remedy_model = RandomForestClassifier()
remedy_model.fit(X_train, y_remedy_train)

exercise_model = RandomForestClassifier()
exercise_model.fit(X_train, y_exercise_train)

# Step 6: Evaluate the models
y_remedy_pred = remedy_model.predict(X_test)
remedy_accuracy = accuracy_score(y_remedy_test, y_remedy_pred)
print(f"Remedy Prediction Accuracy: {remedy_accuracy * 100:.2f}%")

y_exercise_pred = exercise_model.predict(X_test)
exercise_accuracy = accuracy_score(y_exercise_test, y_exercise_pred)
print(f"Exercise Prediction Accuracy: {exercise_accuracy * 100:.2f}%")

# Step 7: User Input
while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be a positive number.")
        break
    except ValueError as ve:
        print(ve)

while True:
    gender = input("Enter your gender (Male/Female): ").strip().lower()
    if gender not in ['male', 'female']:
        print("Please enter either 'Male' or 'Female'.")
    else:
        break

while True:
    injury = input("Enter the injury description: ").strip().lower()
    if len(injury) == 0:
        print("Injury description cannot be empty. Please provide a valid description.")
    else:
        break

# Encode the inputs
try:
    encoded_gender = le_gender.transform([gender])[0]
    encoded_injury = le_injuries.transform([injury])[0]
except ValueError as e:
    print("Error: Entered gender or injury is not in the training dataset. Please try again with valid inputs.")
    exit()

# Create the input data for prediction
new_data = [[age, encoded_gender, encoded_injury]]

# Step 8: Make predictions
predicted_remedy = remedy_model.predict(new_data)
predicted_exercise = exercise_model.predict(new_data)

# Step 9: Display the predicted remedy and exercise
print(f"Predicted Remedy: {predicted_remedy[0]}")
print(f"Predicted Exercise: {predicted_exercise[0]}")

# Step 10: Save the models (Optional)
joblib.dump(remedy_model, 'remedy_model.pkl')
joblib.dump(exercise_model, 'exercise_model.pkl')
