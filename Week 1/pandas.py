import pandas as pd
import numpy as np
 
print(pd.__version__)

#Series- 1d array to hold data of any type

#creating empty series
s=pd.Series()
print(s)

#creating seriees from python lists
lst=[1,2,3]
s2=pd.Series(lst)
print(s2)

#with custom index
s3=pd.Series(lst, index=['a','b','c'])
print(s3)

#creating series from numpy array
arr=np.array([11,22,33])
s4=pd.Series(arr)
print(s4)

#with custom index
arr=np.array([11,22,33])
s4=pd.Series(arr, index=['one','two','three'])
print(s4)

#creating series from dict
dict={'apple':2,'banana':3, 'orange':4}
s5=pd.Series(dict)
print(s5)

#retrieving data from series
#first element
print(s5[0])

#first 3 elements
print(s5[:3])

#last three elements
print(s5[-3:])

#retrieving data using label
print(s5['apple'])

print(s5[['apple','orange']])

#DataFrame- 2d labeled data structures with columns of different types

#creating empty datafrmes
df=pd.DataFrame()
print(df)

#creating dataframe from lists
lst1=['blue', 'green','yellow']
df1=pd.DataFrame(lst1)
print(df1)

#from dict of list
dict_of_lst={'fruit':['apple','pear','mango'],'quantity':[6,7,8]}
df=pd.DataFrame(dict_of_lst)
print(df)

#from dictionary of series
Name=pd.Series(['lynda','Glenn','Clair'])
Age=pd.Series([12,12,13])
dict2={'Name':Name,'Age':Age}
df=pd.DataFrame(dict2)
print(df)

#column and row operation in dataframe

#column addition
df['ID']=pd.Series([1112,1113,1114])
print(df)

#column deletion
del df['ID']
print(df)

#row addition
data=pd.DataFrame([['Jo',15,1115]],columns=['Name','Age','ID'])
print(df.append(data))

#row deletion
df.drop(2)
print(df)

#series basic functionalities

print(s5.axes)

print(s5.ndim)

print(s5.empty)

print(s5.size)

print(s5.values)

print(s5.head(2))

print(s5.tail(2))

#dataframe basic functionalities

print(df1.T)

print(df1.axes)

print(df1.dtypes)

print(df1.empty)

print(df1.ndim)

print(df1.shape)

print(df1.size)

print(df1.head(2))

print(df1.tail(2))

#operations on dataframe

Name=pd.Series(['lynda','Glenn','Clair','Jo','John'])
Age=pd.Series([12,12,13,13,14])
ID=pd.Series([1112,1113,1114,1115,1116])

df3=pd.DataFrame({'Name':Name,'Age':Age,'ID':ID})
print(df3)

print(df3.sum())

#1=axis value=row
print(df3.sum(1))

#mean=average
print(df3.mean())

#std=standard deviation of numerical columns
print(df3.std())

#min=returns min value in each column
print(df3.min())

#max value in each column
print(df3.max())

#count=total number of entries
print(df3.count())

#describe- overall info of numerical column
print(df3.describe())

#indexing and slicing

#select all rows for a specific column
print(df3.loc[:,'Age'])

#select all rows for multiple column
print(df3.loc[:,['Name','ID']])

#select few rows for multiple columns
print(df3.loc[[0,1],['Name','Age']])

#integer slicing
print(df3.iloc[:4])

print(df3.iloc[1:3,1:4])

#dealing with missing data

name= pd.Series(['Ved','Shri','Sam','Ro'])
age= pd.Series([19,np.nan, 22,np.nan])
#nan=not a number
dfnew=pd.DataFrame({'Name':name,'Age':age})
print(dfnew)

#finding missing values
print(dfnew.isnull())

print(dfnew['Age'].isnull())

print(dfnew['Age'].notnull())

#count of null values
print(dfnew['Age'].isnull().sum())

#count for non null values
print(dfnew['Age'].notnull().sum())

#replacing nan with a scalar value
print(dfnew.fillna(0))

#replacing nan with mea value
avg=dfnew['Age'].mean()
#to round off mean value
avg=round(avg,0)
print(dfnew.fillna(avg))

#filling nan with forward and backward values
#filling nan with the value next to it
print(dfnew.fillna(method='backfill'))

#filling nan with the value previous to it
print(dfnew.fillna(method='pad'))

#dropping a missing value
print(dfnew.dropna())

#to replace a value in dataframe
print(dfnew.replace({22:20}))

#groupby- split apply combine
data={'Name':['a','b','c','d','e','f'],'Age':[12,22,62,23,33,43],'Category':['young','young','adult','mid','mid','adult']}
dfn=pd.DataFrame(data)
print(dfn)

print('\n',dfn.groupby('Category'))

print('\n',dfn.groupby('Category').groups)

#retrieving data of each group

group=dfn.groupby('Category')
for name,grp in group:
    print('\n',name)
    print('\n',grp)

#selecting a single group
print('\n', group.get_group('young'))

#aggregations
print('\n',group.count())

print('\n',group.first())
print('\n',group.last())

print('\n',group['Age'].mean())
print('\n',group['Age'].median())
print('\n',group['Age'].max())
print('\n',group['Age'].min())

#multiple aggregations in a single statement
print(group['Age'].agg([np.sum,np.prod,np.std,np.var]))






