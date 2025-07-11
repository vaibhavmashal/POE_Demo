# Classification using KNN algorithm
import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\admin\\Desktop\\datasets\\Iris.csv")
df
X=df.drop(["iris_fl"], axis=1)
y=df["iris_fl"]
min(X["sepal_len"])
max(X["sepal_len"])
min(X["petal_len"])
max(X["petal_len"])
min(X["petal_wid"])
max(X["petal_wid"])
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled=scaler.fit_transform(X)
X_scaled
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y,
test_size=0.2, random_state=42)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
y_pred = knn.predict(X_test)
y_pred
import sklearn.metrics
lbs=['Iris-versicolor', 'Iris-setosa', 'Iris-virginica']
print(sklearn.metrics.confusion_matrix(y_test, y_pred, labels=lbs))
print(sklearn.metrics.accuracy_score(y_test, y_pred))
print(sklearn.metrics.precision_score(y_test, y_pred, labels=lbs,
average='macro'))
print(sklearn.metrics.recall_score(y_test, y_pred, labels=lbs,
average='macro'))
print(sklearn.metrics.f1_score(y_test, y_pred, labels=lbs,
average='macro')) 