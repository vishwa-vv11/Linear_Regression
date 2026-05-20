import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib

#dataset
df=pd.read_csv("marks dataset.csv")
x=df[["Study Hours"]]
y=df["Marks Scored"]

#model
model=LinearRegression()
model.fit(x,y)

#get wight and bias
print("Weight:",model.coef_[0])
print("Bias:",model.intercept_)

#save model
joblib.dump(model,"marks_prediction.pkl")
print("Model saved successfully.")

#predict 
y_pred = model.predict(x)

# Plot actual data
plt.scatter(x, y, label="Actual Data")

#plot predicted data
plt.plot(x, y_pred, color='red', label="Predicted Line")

#labels
plt.xlabel("Study Hours")
plt.ylabel("Marks Scored")
plt.title("Study Hours vs Marks Scored")

#show 
plt.legend()

#display
plt.show()
