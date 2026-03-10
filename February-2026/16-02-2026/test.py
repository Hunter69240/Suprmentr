import pandas as pd
import numpy as np

data={
    'Name':['navya','arjun','riya','arjun',None],
    'Age':[23,25,None,25,22],
    'Salary':[50000,None,45000,60000,48000],
    'Department':['IT','HR','IT','HR','IT']
}

df=pd.DataFrame(data)

# print(df.shape)
# print(df.columns)
# print(df.info)
# print(df.describe)

# df['Department']=df['Department'].str.upper()
# print(df)

#Missing values
'''
Nan- Not a number
None
empty cells
'''

# print(df.isnull().sum())

# print(df.dropna())

# print(df.dropna(axis=1))
#axis 0->rows
#axis 1 ->cols

#filling missing value
#Numerical cols ->mean/median

#mean -> no outliers
#median -> outliers
# df['Age'].fillna(df['Age'].mean(),inplace=True)
# df['Salary'].fillna(df['Salary'].mean(),inplace=True)


# df['Department'].fillna(df['Department'].mode()[0],inplace=True)
# print(df)


'''
DATA PREPROCESSING
convert data to model-ready format
'''

# #1.Encoding categorical data
# df=pd.get_dummies(df,columns=['Department'])
# print(df)

#Feature scaling
#Normalization(0 to 1)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
df[['Age','Salary']]=scaler.fit_transform(df[['Age','Salary']])

#standardization (mean=0,std=1)

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
df[['Age','Salary']]=scaler.fit_transform(df[['Age','Salary']])

#Removing outliers

q1=df['Salary'].quantile(0.25)
q3=df['Salary'].quantile(0.75)

IQR=q3-q1

df=df[(df['Salary']>=q1-1.5*IQR) & (df['Salary']<=q3+1.5*IQR)]

#splitting data,train and test data
'''
Outliers:data that is very far from datapoints
types:
1.Global ->very far from entire dataset
2.Contextual ->normal in one context , abnormal in other context
3.Collective ->a group behaving abnormally

IQR - InterQuartile Range

'''

#Normalization 

'''
normalization is scaling data to fixed range usually 0 to 1
Makes them comparable

formula used =>
x_new=(x-x_min)/(x_max-x_min)
results between 0 to 1
'''


#Standardization
'''
it is nothing but which transforms data so that mean =0,std=1
does not restrict values to 0 and 1

formula  - zscore

z=(X-mean)/std


'''