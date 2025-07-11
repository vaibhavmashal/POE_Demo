# Support Vector Machines (SVM) Algorithm

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Step 2: Load dataset
df = pd.read_csv("C:\\Users\\admin\\Desktop\\datasets\\Iris.csv")

# Rename columns for easier access (optional but useful)
df.rename(columns={
    'sepal_length': 'sepal_len',
    'sepal_width': 'sepal_wid',
    'petal_length': 'petal_len',
    'petal_width': 'petal_wid',
    'species': 'iris_fl'
}, inplace=True)

# Step 3: Encode target labels
le_iris_fl = LabelEncoder()
df['iris_fl_n'] = le_iris_fl.fit_transform(df['iris_fl'])

# Step 4: Prepare input and target
X = df.drop(['iris_fl', 'iris_fl_n'], axis='columns')
y = df['iris_fl_n']

# Step 5: Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 6: Train and evaluate various SVM models
# Default model
model = SVC()
model.fit(X_train, y_train)
print("Default SVC score:", model.score(X_test, y_test))

# SVM with C=1
model_C = SVC(C=1)
model_C.fit(X_train, y_train)
print("SVC with C=1 score:", model_C.score(X_test, y_test))

# SVM with C=0.1
model_C0_1 = SVC(C=0.1)
model_C0_1.fit(X_train, y_train)
print("SVC with C=0.1 score:", model_C0_1.score(X_test, y_test))

# SVM with gamma=10
model_gamma = SVC(gamma=10)
model_gamma.fit(X_train, y_train)
print("SVC with gamma=10 score:", model_gamma.score(X_test, y_test))

# SVM with linear kernel
model_kernel_linear = SVC(kernel='linear')
model_kernel_linear.fit(X_train, y_train)
print("SVC with linear kernel score:", model_kernel_linear.score(X_test, y_test))

# Step 7: Visualizations
df0 = X[:50]
df1 = X[50:100]
df2 = X[100:]

# Sepal Length vs Sepal Width
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Sepal Length vs Width")
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal_len'], df0['sepal_wid'], color="green", marker='+', label='Setosa')
plt.scatter(df1['sepal_len'], df1['sepal_wid'], color="blue", marker='.', label='Versicolor')
plt.scatter(df2['sepal_len'], df2['sepal_wid'], color="black", marker='*', label='Virginica')
plt.legend()

# Petal Length vs Petal Width
plt.subplot(1, 2, 2)
plt.title("Petal Length vs Width")
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.scatter(df0['petal_len'], df0['petal_wid'], color="green", marker='+', label='Setosa')
plt.scatter(df1['petal_len'], df1['petal_wid'], color="blue", marker='.', label='Versicolor')
plt.scatter(df2['petal_len'], df2['petal_wid'], color="black", marker='*', label='Virginica')
plt.legend()

plt.tight_layout()
plt.show()
