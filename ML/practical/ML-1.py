# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a pandas Series
S = pd.Series([11, 28, 72, 3, 5, 8])
print(S)

# Accessing index and values of the Series
print("Index:", S.index)
print("Values:", S.values)

# Creating a NumPy array and comparing with Series values
X = np.array([11, 28, 72, 3, 5, 8])
print("NumPy Array:", X)
print("Series Values:", S.values)

# Checking types
print("Types:", type(S.values), type(X))  # both are <class 'numpy.ndarray'>

# Creating a labeled Series for fruits
fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 33, 52, 10]
S_fruits = pd.Series(quantities, index=fruits)
print(S_fruits)

# Accessing specific value
print("Apples quantity:", S_fruits['apples'])

# Plotting basic graphs
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# Adding labels and title
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("First Plot")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()
