# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:08:55 2019

@author: v072306
"""

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

k=input("Enter the list of values: ")
y = list(map(int, k.split(",")))
t = tuple(y)
print(y)
print(t)