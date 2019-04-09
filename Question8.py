# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:04:21 2019

@author: v072306
"""

"""
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

#k=input("Enter the list of values: ")
#y=[]
#y=list(k.split(","))
#print(y)
#y.sort()
#print(y)

k=['a', 'z', 'b', 'y', 'c', 'x']
k.sort()
print(k)