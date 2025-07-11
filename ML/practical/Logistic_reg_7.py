import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import math

df = pd.read_csv("C:\\Users\\admin\\Desktop\\datasets\\insurance_data.csv")
print(df.head())

# Step 3: Visualize data
plt.scatter(df.age, df.bought_insurance, marker='+', color='red')
plt.xlabel("Age")
plt.ylabel("Bought Insurance")
plt.title("Age vs Insurance Purchase")
plt.show()

# Step 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, test_size=0.1)

# Step 5: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
print("Predictions:", model.predict(X_test))
print("Model Accuracy:", model.score(X_test, y_test))
print("Predicted Probabilities:\n", model.predict_proba(X_test))
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

# Step 7: Manual prediction using sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def prediction_function(age):
    z = model.coef_[0][0] * age + model.intercept_[0]
    y = sigmoid(z)
    return y

# Test the manual prediction function
print("Prediction for age 35:", prediction_function(35))
print("Prediction for age 43:", prediction_function(43))
