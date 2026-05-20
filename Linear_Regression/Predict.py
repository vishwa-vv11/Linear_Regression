import joblib
import numpy as np 
import pandas as pd

#load model
model=joblib.load("marks_prediction.pkl")

#predict
prediction = model.predict([[12]])

#print
print("Predicted Marks Scored for 12 Study Hours:", prediction[0])