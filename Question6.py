# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:06:57 2019

@author: v072306
"""

"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

import numpy as np

res=[]
C=50
H=30
k=input("Enter the list of values: ")
y = list(map(int, k.split(",")))
for D in y:
    res.append(np.round(np.sqrt((2*C*D)/H)))

print(res)