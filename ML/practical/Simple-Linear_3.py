# Simple Linear Regression using Salary Prediction dataset
import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\admin\\Desktop\\dataset\\Salary Data.csv")
df
df.describe()
df=df.dropna()
from sklearn.linear_model import LinearRegression
model = LinearRegression()
X = df[['Years of Experience']]
y = df['Salary']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.2,random_state=42)
model.fit(X_train,y_train)
model.predict(X_test)
model.score(X_test,y_test) 