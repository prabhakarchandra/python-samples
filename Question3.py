# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:02:02 2019

@author: v072306
"""

# Question 3
# Level 1

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

k=int(input("Enter the integer value for dictionary creation: "))

def sqfunc(y):
    return y * y

d={}

for i in range(1, k+1):
    d[i] = sqfunc(i)
    
print(d)
    
