# Decision Tree Classifier implementation
import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\admin\\Desktop\\dataset\\iris.data",
header=None)
df
df.columns=["Sepal LengthCm", "SepalwidthCm", "PetalLengthCm",
"PetalWidthCm", "Class"]
df
X=df.drop(["Class"], axis=1)
y=df["Class"]
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y=le.fit_transform(y)
y
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=42)
from sklearn.tree import DecisionTreeClassifier
dcl=DecisionTreeClassifier(criterion='entropy')
dcl.fit(X_train,y_train)
dcl.score(X_test,y_test)
from sklearn import tree
import matplotlib.pyplot as plt
tree.plot_tree(dcl)
plt.show() 
