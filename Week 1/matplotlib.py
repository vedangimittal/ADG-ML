
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


mall=pd.read_csv('Mall_Customers.csv')
print(mall)

print(mall.head())

table=pd.pivot_table(data=mall,index='Age',values='Spending Score (1-100)',aggfunc=np.sum)
print(table)

table2=pd.pivot_table(data=mall,index='Genre',values='Spending Score (1-100)',aggfunc=np.sum)
print(table2)

#bar graph
plt.bar(table2.index,table2['Spending Score (1-100)'],width=0.5)

#x axis label
plt.xlabel('Gender')
#y axis label
plt.ylabel('Spending Score')
#plot title
plt.title('Gendre wise spending score analysis')
#if ticks are overlaping use plt.xticks(rotation=(specify angle))
#showing plot
plot=plt.show()

from numpy import genfromtxt

arr=np.genfromtxt('Mall_Customers.csv', delimiter=',',skip_header=0)
print(arr)

sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
for i in arr:
    if i[2]<=18 and i[2]<=20:
            sum1=i[3]+sum1
    elif i[2]<=21 and i[2]<=30:
        sum2=i[3]+sum2
    elif i[2]<=31 and i[2]<=40:
        sum3=i[3]+sum3
    elif i[2]<=41 and i[2]<=50:
        sum4=i[3]+sum4
    elif i[2]<=51 and i[2]<=60:
        sum5=i[3]+sum5
    elif i[2]<=61 and i[2]<=70:
        sum6=i[3]+sum6

lst=[sum1,sum2,sum3,sum4,sum5,sum6]
spendsum=np.array(lst)
print(spendsum)

ages=['ages 18-20','ages 21-30','ages 31-40','ages 41-50','ages 51-60','ages 61-70']
plt.pie(spendsum,labels=ages,explode=(0,0,0.1,0.2,0,0),radius=1.2)
plt.title('Age wise spending score analysis')
plt.show()


