# Program-1 (Method-I: Creating DataFrame)
import pandas as pd
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj', 'Ravi', 'Natasha',
'Riya'],
 'Age': [17, 17, 18, 17, 18, 17, 17],
 'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
 'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]}
df = pd.DataFrame(data)
df
# Program-2 (Method-II: Uploading csv file)
import pandas as pd
df = pd.read_csv(r'E:\ml datasets Machine-Learning-with-Pythonmaster\Datasets\loan_data.csv')
print(df.head())
# Filtering the data
df.filter(['Name'])
df.filter(['Age'])
df[df['Age']==17]
df.filter(['Marks'])
df[df['Marks']==76]
df[['Name','Gender','Marks']][df['Age']==17]
# Merging
details = pd.DataFrame({
 'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
 'NAME': ['Jagroop', 'Praveen', 'Harjot', 'Pooja', 'Rahul',
'Nikita', 'Saurabh', 'Ayush', 'Dolly', 'Mohit'],
 'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE', 'CSE', 'CSE', 'CSE', 'CSE',
'CSE', 'CSE']
})
fees_status = pd.DataFrame({
 'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
 'PENDING': [5000, 250, 'NIL', 9000, 15000, 'NIL', 4500, 1800, 250,
'NIL']
})
print(pd.merge(details, fees_status, on='ID'))
# Handling the missing values:
import pandas as pd
import numpy as np
fees_status = pd.DataFrame({
 'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
 'PENDING': [5000, 250, 'NIL', 9000, 15000, 'NIL', 4500, 1800, 250,
'NIL']
})
df.replace(to_replace='NaN', value=np.nan)
df.fillna(value=0)
df.fillna(method='pad')
df.fillna(method='bfill') 