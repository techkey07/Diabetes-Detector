# Diabetes Detector using Machine Learning

## 1. Project Overview

This project is a simple machine learning program that predicts whether a person is diabetic or not.
The program uses medical information such as glucose level, blood pressure, BMI, and age to make the prediction.

The goal of this project is to show the basic steps of building a machine learning system:

* Loading a dataset
* Training a model
* Testing the model
* Making predictions

The model is trained using the **Pima Indians Diabetes Dataset** from Kaggle.

---

## 2. Why This Project Matters

Diabetes is a common health condition that affects many people. Early detection can help people take proper treatment and manage their health better.

Machine learning can help analyze patient data and predict the chances of diabetes. This project demonstrates how a simple ML model can be used for that purpose.

---

## 3. Dataset Information

The dataset used in this project contains medical information about patients.

Each row represents one patient.

### Features in the dataset

* Pregnancies – Number of times the patient was pregnant
* Glucose – Blood glucose level
* BloodPressure – Blood pressure value
* SkinThickness – Thickness of skin fold
* Insulin – Insulin level
* BMI – Body Mass Index
* DiabetesPedigreeFunction – Family history of diabetes
* Age – Age of the patient

### Target Variable

Outcome

* 0 → Person is not diabetic
* 1 → Person is diabetic

---

## 4. Technologies Used

This project was built using the following tools:

* Python
* Pandas
* NumPy
* Scikit-learn

---


## 5. How the Project Works

The program follows these steps:

1. The dataset is loaded using the Pandas library.
2. The dataset is divided into input features and output labels.
3. The data is split into training data and testing data.
4. A Logistic Regression model is created.
5. The model is trained using the training dataset.
6. The model is tested using the testing dataset.
7. The program calculates the model accuracy.
8. The user enters patient medical details.
9. The model predicts whether the person is diabetic or not.


---

## 6. How to Run the Project

Run the Python program using the command:

python diabetes_detector.py

The program will start and ask you to enter patient medical details.

---

## 7. Example Input

Pregnancies: 2
Glucose Level: 120
Blood Pressure: 70
Skin Thickness: 20
Insulin Level: 80
BMI: 25
Diabetes Pedigree Function: 0.5
Age: 30

---

## 8. Example Output

Prediction Result: Person is NOT DIABETIC

---

## 9. What I Learned From This Project

While working on this project, I learned:

* How machine learning models are built
* How datasets are used for training models
* How to split data into training and testing sets
* How to measure model accuracy
* How to make predictions using user input

---

## 10. Future Improvements

This project can be improved in the future by:

* Adding data visualization graphs
* Improving model accuracy
* Creating a web interface for easier use
* Deploying the model as an online application

---
