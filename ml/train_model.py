import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Define file path
file_path = r"C:\Users\thiya\OneDrive\Documents\pdlproject\ml\expanded_dataset.xlsx"

# Check if dataset file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ Dataset file not found at: {file_path}")

print("📂 Loading dataset...")
dataset = pd.read_excel(file_path)

# Check for missing values
if dataset.isnull().sum().sum() > 0:
    print("⚠️ Warning: Dataset contains missing values. Filling with mode.")
    dataset.fillna(dataset.mode().iloc[0], inplace=True)

# Initialize encoders
le_gender = LabelEncoder()
le_injury = LabelEncoder()
le_remedy = LabelEncoder()
le_exercise = LabelEncoder()

# Fit and transform categorical data
dataset["gender"] = le_gender.fit_transform(dataset["gender"])
dataset["injury"] = le_injury.fit_transform(dataset["injury"])
dataset["remedy"] = le_remedy.fit_transform(dataset["remedy"])
dataset["exercise"] = le_exercise.fit_transform(dataset["exercise"])

# Define features & labels
X = dataset[["age", "gender", "injury"]]
y_remedy = dataset["remedy"]
y_exercise = dataset["exercise"]

# Train-test split
X_train, X_test, y_remedy_train, y_remedy_test = train_test_split(X, y_remedy, test_size=0.2, random_state=42)
X_train, X_test, y_exercise_train, y_exercise_test = train_test_split(X, y_exercise, test_size=0.2, random_state=42)

# Train models
print("🛠️ Training models...")
remedy_model = RandomForestClassifier(n_estimators=100, random_state=42)
remedy_model.fit(X_train, y_remedy_train)

exercise_model = RandomForestClassifier(n_estimators=100, random_state=42)
exercise_model.fit(X_train, y_exercise_train)

# Save models and encoders
print("💾 Saving models & encoders...")
joblib.dump(remedy_model, "remedy_model.pkl")
joblib.dump(exercise_model, "exercise_model.pkl")
joblib.dump(le_gender, "le_gender.pkl")
joblib.dump(le_injury, "le_injury.pkl")
joblib.dump(le_remedy, "le_remedy.pkl")
joblib.dump(le_exercise, "le_exercise.pkl")

print("✅ Models trained and saved successfully!")
