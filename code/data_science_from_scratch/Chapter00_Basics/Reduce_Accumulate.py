# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:59:42 2019

@author: admin

@source : https://www.geeksforgeeks.org/reduce-in-python/

"""

# ------------------------------------------------------
# Section 01 : Using lambda
# ------------------------------------------------------

import functools as ft

myList = [1,2,3,4,5]

# note : lamda fun is the first argument to reduce, myList is the seq as second arg
print(ft.reduce(lambda a, b : a + b, myList))


import itertools as itt

print(f"myList : {myList}")
for i in itt.accumulate(myList, lambda a, b : a + b):
    print(i)

# ------------------------------------------------------
# Section 02 : Using Operator
# ------------------------------------------------------

import operator
print(ft.reduce(operator.add, myList))

for i in itt.accumulate(myList, operator.add):
    print(i)
