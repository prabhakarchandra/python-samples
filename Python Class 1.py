# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:04:21 2018

"""

print("hello world")

print("Shailen'dra")


4+9



2+3

6.09912345/2

6-9

1+(2*3)



8%2



#I am doing this for checking how comments work
abcd = []

# list of integers
abcd = [1, 2, 3,"shail"]

print(abcd)



print("jackie's dog")


# list with mixed datatypes
mixedlist = [9, "Shail", 67.4,0]

# nested list
nestedlist = ["shail", [11,8, 4, 6], ['toronto'],abcd, "abcd"]
print(nestedlist)

#arrays

arr1 = [10, 20, 30, 40, 50, 100]

print(arr1[5])



arr2 = [100, 200, 300, 400, 500,1000]

arr3 = arr1+arr2
print(arr3)
#selecting and printing a specific element from an array
print(arr1[2])


# Negative indexing
print(arr3[-1])

#length of array

len(arr3)






#Adding another element

newarr = [100,120]
newarr.append(200)
print(newarr)

 
#indentation


for i in range(1,11):
    csq=i*i    

    print (csq)
    
    
 #If and else   

myname="Andy"

if myname == 'Shailendra':
    print ('Correct')
else:
    print ("error")
    
    
dig =20

if dig == 20:
    print ('Correct')
else:
    print ("error")





N = 18

if N%2 ==1:
    print("odd")
elif N%2 ==0 and (2<=N<=5):
    print("Even but within 5")
elif N%2 ==0 and (6<=N<=20):
    print("between 6 and 20 even")
elif N%2 ==0 and N>20:
    print("even more than 20")
    
    
    
n = 34

for x in range(0,n):
    print(x*x)
    

n = 21
    
for i in range(0,n):
    print(i+1,end ="")


    
import numpy


import numpy

a= numpy.array([1,2,3,4])
b = numpy.array([5,6,7,8])

a1= numpy.array([a+b])
a2= numpy.array([a-b])
a3= numpy.array([a*b])

a4= numpy.array([a//b])
a5= numpy.array([a%b])
a6= numpy.array([a**b])





print (a1)
print(a2)
print(a3)
#print(a4)
print(a5)
print(a6)