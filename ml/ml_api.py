from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import os

# Check if all required files exist
required_files = ["remedy_model.pkl", "exercise_model.pkl", "le_gender.pkl", "le_injury.pkl"]
missing_files = [file for file in required_files if not os.path.exists(file)]

if missing_files:
    raise FileNotFoundError(f"❌ Missing files: {missing_files}. Run train_model.py first.")

# Load the trained models and label encoders
remedy_model = joblib.load("remedy_model.pkl")
exercise_model = joblib.load("exercise_model.pkl")
le_gender = joblib.load("le_gender.pkl")
le_injury = joblib.load("le_injury.pkl")
le_remedy = joblib.load("le_remedy.pkl")
le_exercise = joblib.load("le_exercise.pkl")

app = FastAPI()

# Define request structure
class PredictionRequest(BaseModel):
    age: int
    gender: str
    injury: str

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        # Encode gender and injury
        if request.gender not in le_gender.classes_:
            return {"error": f"Unknown gender: {request.gender}"}
        if request.injury not in le_injury.classes_:
            return {"error": f"Unknown injury: {request.injury}"}

        encoded_gender = le_gender.transform([request.gender])[0]
        encoded_injury = le_injury.transform([request.injury])[0]

        # Prepare input data
        input_data = [[request.age, encoded_gender, encoded_injury]]

        # Predict remedy and exercise
        predicted_remedy_encoded = remedy_model.predict(input_data)[0]
        predicted_exercise_encoded = exercise_model.predict(input_data)[0]

        # Decode predictions
        predicted_remedy = le_remedy.inverse_transform([predicted_remedy_encoded])[0]
        predicted_exercise = le_exercise.inverse_transform([predicted_exercise_encoded])[0]

        return {"remedy": predicted_remedy, "exercise": predicted_exercise}

    except Exception as e:
        return {"error": str(e)}
