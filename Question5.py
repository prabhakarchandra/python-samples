# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:01:10 2019

@author: v072306
"""

"""
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""

class testClass(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s=input("Enter the string value: ")
    def printString(self):
        print(self.s)
        
strObj = testClass()
strObj.getString()
strObj.printString()
