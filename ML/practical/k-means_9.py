
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt


df = pd.read_csv("C:\\Users\\Admin\\Downloads\\Data science\\income.csv")
print(df.head())

plt.figure(figsize=(6, 4))
plt.scatter(df['Age'], df['Income($)'])
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title("Age vs Income (Before Clustering)")
plt.show()

km = KMeans(n_clusters=3, random_state=42, n_init=10)
y_predicted = km.fit_predict(df[['Age', 'Income($)']])
df['cluster'] = y_predicted

# Step 5: Visualize clusters (before scaling)
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

plt.figure(figsize=(6, 4))
plt.scatter(df1.Age, df1['Income($)'], color='green', label='Cluster 0')
plt.scatter(df2.Age, df2['Income($)'], color='red', label='Cluster 1')
plt.scatter(df3.Age, df3['Income($)'], color='black', label='Cluster 2')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title("Clusters (Before Scaling)")
plt.legend()
plt.show()

# Step 6: Scale the data
scaler = MinMaxScaler()

df['Income($)'] = scaler.fit_transform(df[['Income($)']])
df['Age'] = scaler.fit_transform(df[['Age']])

# Step 7: Reapply KMeans on scaled data
km = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = km.fit_predict(df[['Age', 'Income($)']])

# Step 8: Visualize clusters (after scaling)
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

plt.figure(figsize=(6, 4))
plt.scatter(df1.Age, df1['Income($)'], color='green', label='Cluster 0')
plt.scatter(df2.Age, df2['Income($)'], color='red', label='Cluster 1')
plt.scatter(df3.Age, df3['Income($)'], color='black', label='Cluster 2')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title("Clusters (After Scaling)")
plt.legend()
plt.show()
