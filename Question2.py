# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:53:53 2019

@author: v072306
"""

# Question2: Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
    
k = input("Enter the value to find factorial for: ")
i = 1
res = 1
while (i <= int(k)):
    res = res * i
    i = i + 1
print("The factorial of the input value is: " + str(res))