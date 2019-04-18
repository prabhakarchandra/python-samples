# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:34:01 2019

@author: Prabhakar Chandrasekaran
"""

def binary_search(sorted_collection, item):
    """Binary search algorithm using while loop.
    :param sorted_collection: some sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None


print(binary_search([0, 2, 3, 5, 8, 9], 5))
print(binary_search([4, 8, 12, 16, 20], 20))
print(binary_search([6, 8, 9, 11, 13, 22], 6))