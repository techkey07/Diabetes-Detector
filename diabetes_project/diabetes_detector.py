# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("mragpavank/diabetes")

# print("Path to dataset files:", path)


# -------------------------------------------------
# Diabetes Detection using Machine Learning
# Dataset: Pima Indians Diabetes Database
# -------------------------------------------------

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# -------------------------------------------------
# FUNCTION TO SAFELY TAKE NUMERIC INPUT
# -------------------------------------------------

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


# -------------------------------------------------
# STEP 1: LOAD DATASET
# -------------------------------------------------

print("Loading dataset...\n")

data = pd.read_csv("diabetes.csv")

print("Dataset Loaded Successfully!\n")


# -------------------------------------------------
# STEP 2: SHOW DATA INFORMATION
# -------------------------------------------------

print("First 5 rows of dataset:\n")
print(data.head())

print("\nDataset Shape:")
print(data.shape)


# -------------------------------------------------
# STEP 3: SPLIT FEATURES AND TARGET
# -------------------------------------------------

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

print("\nFeatures and target separated.")


# -------------------------------------------------
# STEP 4: SPLIT TRAINING AND TEST DATA
# -------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data size:", X_train.shape)
print("Testing data size:", X_test.shape)


# -------------------------------------------------
# STEP 5: CREATE MODEL
# -------------------------------------------------

model = LogisticRegression(max_iter=1000)

print("\nTraining the model...")


# -------------------------------------------------
# STEP 6: TRAIN MODEL
# -------------------------------------------------

model.fit(X_train, y_train)

print("Model training completed.")


# -------------------------------------------------
# STEP 7: TEST MODEL
# -------------------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)


# -------------------------------------------------
# STEP 8: USER INPUT
# -------------------------------------------------

print("\n----------------------------------")
print("Enter Patient Details")
print("----------------------------------")

preg = get_number("Pregnancies: ")
glucose = get_number("Glucose Level: ")
bp = get_number("Blood Pressure: ")
skin = get_number("Skin Thickness: ")
insulin = get_number("Insulin Level: ")
bmi = get_number("BMI: ")
dpf = get_number("Diabetes Pedigree Function: ")
age = get_number("Age: ")


# -------------------------------------------------
# STEP 9: PREDICTION
# -------------------------------------------------

input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

prediction = model.predict(input_data)


# -------------------------------------------------
# STEP 10: RESULT
# -------------------------------------------------

print("\n----------------------------------")

if prediction[0] == 1:
    print("Prediction Result: Person is DIABETIC")
else:
    print("Prediction Result: Person is NOT DIABETIC")

print("----------------------------------")