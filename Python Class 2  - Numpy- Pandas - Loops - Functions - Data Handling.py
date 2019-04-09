# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import csv
import os


os.getcwd()
os.chdir('D:\\Training Proffesionaly\\Sample Datasets for Students')

os.getcwd()


#loops in python

#ex 1

frus = ["Apple","Peach",30]
for i in frus:
    print(i)
  
  
#Ex 2  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  for y in x:
      print(y)
  
 #Ex 3

for x in range(7):
  print(x+12) 
  
for i in range(9):
    print(i)
  
  
#ex 4

for x in range(2, 6):
  print(x)
 
#ex 5

for x in range(10):
  print(x)
else:
  print("Done till 10!")

    
#ex 6

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#ex 7    
  
list = [10,20,35,50,55,60]
evenlist = []
oddlist = []


for i in list:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
 
print(evenlist)
print(oddlist)                


#While loop
        
count = 0
while (count < 9):     
    count = count + 1
    print(count)
    

count = 0
while (count < 9):     
    count = count + 1
    print("less than 9") 
else: 
    print("More than 9")     
    


#FUNCTIONS========================================


#Defining a function

#Example 1

def greetings(name):
	"""This function greets to the person passed in as	parameter"""
	print("Hello, " + name + ". Good morning!")
   
greetings("Andy")
greetings("Alex")
greetings("Shail")



#Calling a function

greetings("Alis")    

#Example 2

def cube(num):
	"""This function returns the cube of the entered number"""

	if num >= 0:
		return num*num*num
	else:
		return "negative"
    
cube(9)
cube(-9)
cube(724356827)
greetings("Risa")

#Parameters = Information can be passed to functions as parameter.

def my_function(fname):
  print(fname + " is a Data Scientist")

my_function("Demet")
my_function("Chandan")
my_function("Shailendra")
my_function("Alistair")


#Passing value to a function

def my_function(country = "Norway"):
  print("I live in  " + country)

my_function("Canada")
my_function("India")
my_function()
my_function("Brazil")
            
        
#Returning values

def my_function(x):
  return x * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

cube(10)

#Recursive functions

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



#Fibonacci Sequence

"""
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
  
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

    Fn = Fn-1 + Fn-2
with 

   F0 = 0 and F1 = 1.  
    
"""

def Fibon(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibon(n-1)+ Fibon (n-2)
    
Fibon(6)


    


# WORKING WITH EXTERNAL FILES =======================================================================


#importing data from computer and other locations



newdata = pd.read_csv('Sample_csv_File_V1.csv')

#checking the data


#gives stats about numerical variables
checkingdata = newdata.describe()

#allows us to view first X observations
t = newdata.tail()

#getting frequency table of a single variable
newdata['PROGRAMEID'].value_counts()



print(newdata.columns) # prints the column names


# reading a csv file with options

newdata1 = pd.read_csv('Sample_csv_File_V2.csv')

newdata1 = pd.read_csv('Sample_csv_File_V2.csv',dtype=str, delimiter='|')

newdata1.dtypes

newdata1['DateofEvaluation']=pd.to_datetime(newdata1['DateofEvaluation'], format="%m/%d/%y")


#Changing the data type of a variable after reading a file

#newdata1.Revenue = newdata1.Revenue.astype(int)

newdata1.Revenue = newdata1.Revenue.astype(float)

newdata1['Revenue'] = newdata1['Revenue'].astype(float)

newdata1.dtypes

t = newdata1.dtypes

newdata1.PROGRAMEID.unique() # calulating the unique rows

t = newdata1.describe()

#Group by 


newdata1.agg({'Revenue':'mean'})



print(newdata1['Revenue'].mean())

print(newdata1.Revenue.sum())


print(newdata1['Revenue'].median())

print(newdata1['PROGRAMEID'].mode())

print(newdata1['Revenue'].std())

print(newdata1['PROGRAMEID'].count())


abcd = np.percentile(newdata1['Revenue'], [10,20,30,40,80,90,95,99,99.5], axis =0)



#Part 2 =========================   DATA HANDLING ================================================





age = pd.read_csv('Sample_Age.csv',dtype=str, delimiter=',')


#Merging files
newdata2 = pd.merge(newdata1,age, how='left', on='PERSONID' ) #left_on = 'PersonID' right_on = "Person_id'

#Data Exploration


#Changing the data type of a variable after reading a file
newdata2.Age = newdata2.Age.astype(float)


t = newdata2.describe()

#Selecting a few columns from a dataframe

t=newdata2[['PERSONID', 'PROGRAMEID', 'Age']]

newdata2['Age'] = newdata2['Age'].fillna(newdata2['Age'].mean())


#Creating a new variable

newdata2['rev2'] = newdata2['Revenue']*2




newdata2.rev2 = newdata2.Revenue*2

newdata2['rev3'] = newdata2['Revenue'] + newdata2['rev2']


#filtering data

t= newdata2[newdata2['Revenue'] < 110]

t= newdata2.Revenue < 110



# Creating a flag variable

newdata2['Rev_flag'] = np.where(newdata2['Revenue'] > 110, 'GT_110', '<=110')

newdata2['Rev_flag'].unique()

# Dropping a column


t = newdata2.drop(['rev3', 'rev2'], axis = 1)



#excluding rows based on a condition


t = newdata2[newdata2.PROGRAMEID != 'CM-DP']

t = newdata2.drop([0, 1,5,7,9])

t = newdata2.head()

newdata1.shape

#renaming a column

newdata2.rename(columns={'rev2':'total_bill'}, inplace = True)

#sorting a dataset

newdata2 = newdata2.sort_values([ 'Age', 'total_bill'])


#Missing value treatment

newdata2['Age'].fillna(47, inplace = True)

#groupby

Rev_summed = newdata2.groupby(['TRFRNAME']).Revenue.sum()

Age_mean = newdata2.groupby(['TRFRNAME', 'PROGRAMEID']).Age.mean()



#Writing a file to external location as csv
Rev_summed.to_csv("Rev_summed.csv")
  



#creating multiple flags using lambda function

newdata2['age_grp'] = newdata2['Age'].apply(lambda x : 
    'GRP_LE_35' if x <= 35 
    else 'GRP_LE_50' if x > 35 and x <= 50 
    else 'GRP_GT_50' if x > 50 and x <= 173 
    else 'MISS')

newdata2['age_grp'].unique()

#Using SQL in python

from pandasql import *
pysqldf = lambda r: sqldf(r, globals())

r= """
  Select 
  (sum(Revenue))/1000 as rev_sum000
  from newdata2
  """
  
df_test = pysqldf(r)


from pandasql import *
pysqldf = lambda r: sqldf(r, globals())

r= """
  Select 
  PROGRAMEID,
  (sum(Revenue))/1000 as rev_sum000
  from newdata2
  group by PROGRAMEID
  
  """
  
df_test = pysqldf(r)
  


from pandasql import *
pysqldf = lambda r: sqldf(r, globals())

r= """
  Select 
  PROGRAMEID,TRFRID,
  (sum(Revenue))/1000 as rev_sum000,
  sum(Age) as mean_age
  from newdata2
  group by PROGRAMEID,TRFRID
  
  """
  
df_test = pysqldf(r)
  


#Creating a band variable by using SQL
from pandasql import sqldf


from pandasql import *
pysqldf = lambda r: sqldf(r, globals())

r= """
Select *,
CASE When "Revenue" > 150 THEN ">150"
WHEN "Revenue" > 110 THEN ">110"
ELSE "<=110"
END
as "REVBand"
from newdata2
"""
df_test=pysqldf(r)
  


#functions for calculations


def func(x):
    d = {}
    d['count_cust'] = x['PERSONID'].count()
    d['total_age'] = x['Age'].sum()/1000
    
    return pd.Series(d, index=['count_cust',
                                'total_age'])
    
    
    
    
t = newdata2.groupby(['PROGRAMEID','TRFRID']).apply(func).reset_index()


#----------------------------------
#Graphs and diagrams


import numpy as np
import pandas as pd
import csv
import os
from pandasql import sqldf


import matplotlib

from matplotlib import pyplot as plt



olsdata = pd.read_csv('OLS_dataset_new.csv')

t = olsdata.describe()


# Simple Line Graph
plt.scatter(olsdata['CRIM'], olsdata['MEDV'])
plt.xlabel("CRIM")
plt.ylabel("MEDV")

plt.barh(olsdata['CRIM'], olsdata['MEDV'])
plt.xlabel("CRIM")
plt.ylabel("MEDV")



plt.bar(olsdata['CRIM'], olsdata['MEDV'])
plt.xlabel("CRIM")
plt.ylabel("MEDV")


plt.plot(olsdata['CRIM'], olsdata['MEDV'])
plt.xlabel("CRIM")
plt.ylabel("MEDV")

plt.plot(df_test['PROGRAMEID'], df_test['mean_age'])
plt.xlabel("PROGRAMEID")
plt.ylabel("mean_age")


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Cookies', 'Candies', 'Biscuits', 'Others'
sizes = [15, 30, 45, 10]
explode = (0, 0, 0.2, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()





plt.scatter(olsdata['ZN'], olsdata['MEDV'])
plt.xlabel("ZN")
plt.ylabel("MEDV")


plt.scatter(olsdata['INDUS'], olsdata['MEDV'])
plt.xlabel("INDUS")
plt.ylabel("MEDV")



plt.scatter(olsdata['CHAS'], olsdata['MEDV'])
plt.xlabel("CHAS")
plt.ylabel("MEDV")




plt.scatter(olsdata['NOX'], olsdata['MEDV'])
plt.xlabel("NOX")
plt.ylabel("MEDV")



plt.scatter(olsdata['RM'], olsdata['MEDV'])
plt.xlabel("RM")
plt.ylabel("MEDV")



plt.scatter(olsdata['AGE'], olsdata['MEDV'])
plt.xlabel("AGE")
plt.ylabel("MEDV")



plt.scatter(olsdata['DIS'], olsdata['MEDV'])
plt.xlabel("DIS")
plt.ylabel("MEDV")



plt.scatter(olsdata['RAD'], olsdata['MEDV'])
plt.xlabel("RAD")
plt.ylabel("MEDV")



plt.scatter(olsdata['NOX'], olsdata['MEDV'])
plt.xlabel("NOX")
plt.ylabel("MEDV")


plt.scatter(olsdata['TAX'], olsdata['MEDV'])
plt.xlabel("TAX")
plt.ylabel("MEDV")



plt.scatter(olsdata['PTRATIO'], olsdata['MEDV'])
plt.xlabel("PTRATIO")
plt.ylabel("MEDV")


plt.scatter(olsdata['B'], olsdata['MEDV'])
plt.xlabel("B")
plt.ylabel("MEDV")



plt.scatter(olsdata['LSTAT'], olsdata['MEDV'])
plt.xlabel("LSTAT")
plt.ylabel("MEDV")


# Doing it all in one shot using 

def graphs(X,Y):
    plt.plot(olsdata[X],olsdata[Y])
    plt.xlabel("X")
    plt.ylabel("Y")
    
graphs('LSTAT','MEDV')  
graphs('B','MEDV')
graphs('PTRATIO','MEDV')

graphs('B','MEDV')  




#Data visualization


#PLots
import matplotlib

from matplotlib import pyplot as plt

#plotting a simple line
plt.plot([1,3,1.5,8,4,9])

plt.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4])

#plotting multiple lines
plt.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4],
             [0.1, 0.2, 0.3, 0.4], [1, 4, 9, 16])


# Simple Line Graph
plt.plot(df_test['PROGRAMEID'], df_test['rev_sum000'] )
plt.xlabel("PROGRAMEID")
plt.ylabel("rev_sum000")



plt.plot(df_test['PROGRAMEID'], df_test['rev_sum000'],  
         df_test['PROGRAMEID'], df_test['mean_age'] )
plt.xlabel("PROGRAMEID")
plt.ylabel("Rev & Age")








#Simple Bar graph
plt.bar(df_test['PROGRAMEID'], df_test['rev_sum000'])

plt.bar(df_test['PROGRAMEID'], df_test['rev_sum000'], width = .5)


#For Practice

lst = ['a','b','a','c','a','d','r','g','t','s','d','t','w','s','c','f','a','e','d','c','a','e','f','tg','y','h','s','a','r','t','f','s','e','s','d','a','z','a','s','x','a']
def most_common(inp):
    return (max(set(inp), key=inp.count), lst.count(max(set(lst), key=lst.count)))


most_common(lst)



lst.count(most_common(lst))


def least_common(lst):
    return (min(set(lst), key=lst.count), lst.count(min(set(lst), key=lst.count)))

least_common(lst)
















