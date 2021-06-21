# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:30:23 2019

@author: admin

@source : https://www.learnpython.org/en/Partial_functions

"""

def myFunc (arg1, arg2, arg3):
    return(print(f"arg1 : {arg1} arg2 : {arg2} arg3 : {arg3}"))

print(myFunc('value1', 'value2', 'value3'))

from functools import partial

# using partial, the arguments are assigned left to right
# the myNewFunc will accet two args only
myNewFunc = partial(myFunc, 'NewValue1')

print(myNewFunc('NewvaluePassed2', 'NewvaluePassed3'))
