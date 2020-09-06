
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

#plotting a line
x=[1,12,13,45,6,77]
y=[2,3,4,56,78,9]

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('line graph')
plt.plot(x,y)
plt.show()

#plotting two or more lines
x1=['maths','physics','chemistry']

y1=[99,67,85]
plt.plot(x1,y1,label='david')

y2=[23,56,45]
plt.plot(x1,y2,label='john')

y3=[25,55,89]
plt.plot(x1,y3,label='clair')

plt.xlabel('subjects')
plt.ylabel('score')

#use legend to show info about the type of line and its colour
plt.legend()
plt.show()

#scatter plot- used to plot data points
xs=[1,2,3,4,5,6,7,8,9]
ys=[1,4,9,16,36,50,50,50,50]

plt.scatter(xs,ys,label='stars',color='blue',marker='3',s=100)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('scatter plot')

plt.legend()

plt.show()

#pie chart

items=['apple','sony','samsung','oneplus','motorola']
proportions=[30,25,20,15,10]

colours=['r','y','g','b','m']

plt.pie(proportions, labels=items, colors=colours, startangle=45, 
        shadow=True, explode=(0.2,0.1,0,0,0), radius=1.2, autopct='%1.1f%%')
#startangle- rotates the pie chart by angle degrees counterclockwise from x ais

plt.title('marketplace')
plt.legend()
plt.show()

#bar graph
xb=[1,2,3,4]
yb=[23,45,78,12]

tick_label=['one','two','three','four']

plt.bar(xb, yb, tick_label=tick_label, width=0.5,
        color=['red','green','blue','yellow'])

plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.title('Bar graph')

plt.show()

#horizontal graph
plt.barh(xb, yb, tick_label=tick_label,
        color=['red','green','blue','yellow'])

#histogram

#y axis
ages=[12,23,12,34,45,67,78,76,54,3,22,34,55,66,14,23,10,20,80]

#range-units on x-axis
range=(0,100)

#bins-number of bar graphs we want
bins=20

g=plt.hist(ages,bins,range,color='m',histtype='bar',rwidth=0.5)
#histtype- bar, barstacked, step, stepfilled

plt.xlabel('number of people')
plt.ylabel('ages of people')

plt.show(g)

#customization
plt.plot(x,y,color='g',linestyle='dashed',linewidth=3,marker='o',
         markerfacecolor='blue',markersize=12)

