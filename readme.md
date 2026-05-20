Study Hours vs Marks Prediction using Linear Regression

A beginner-friendly Machine Learning project that predicts student marks based on study hours using Linear Regression.

Project Overview

This project demonstrates how Linear Regression works using a synthetic dataset of:

Study Hours
Marks Scored

The model learns the relationship between:

more study hours → higher marks

and predicts marks for new study hours.

Features

✅ Synthetic dataset generation
✅ CSV dataset loading using Pandas
✅ Linear Regression model training
✅ Weight and Bias calculation
✅ Regression graph visualization
✅ Model saving using Pickle (.pkl)
✅ Prediction using saved model

Technologies Used
Python
Pandas
NumPy
scikit-learn
Matplotlib
Joblib

Dataset
Study Hours	Marks Scored
1	35
2	40
3	50
4	55
5	60
6	68
7	72
8	80
9	88
10	95
Linear Regression Equation

The model uses:

y=wx+b
w
b

Where:

x = study hours
y = predicted marks
w = weight/slope
b = bias/intercept

Learned equation:

y=6.58x+28.11


Clone the repository:

git clone <your-repository-url>

Move into project directory:

cd Study_Hours_Prediction

Install dependencies:

pip install -r requirements.txt
Train the Model

Run:

python train.py

This will:

load dataset
train model
display regression graph
save trained model
Predict Using Saved Model

Run:

python predict.py

Example prediction:

Predicted Marks: 107.07
Visualization

The regression line shows the relationship between:

study hours
marks scored

Example:

4
Model Saving

The trained model is saved as:

linear_regression_model.pkl

This allows prediction without retraining.