# -*- coding: utf-8 -*-

"""
Created on Fri Dec  6 13:26:48 2019

@author: admin

@source : https://www.geeksforgeeks.org/args-kwargs-python/

@description : the script explains usage of *args (var args) and **kwargs (keyworded var args)

"""

# ---------------------------------------------------------------------------------------------------------------------
# Part 01 : Simple use of *args
# ---------------------------------------------------------------------------------------------------------------------

# *args means that the function can accepts any number of arguments
# to retrieve the value use for loop or similar approach

def addSetOfNumber (*setOfNumbersToAdd):

    retVal = 0
    for inputNumber in setOfNumbersToAdd:
        retVal += inputNumber;

    return retVal

print(addSetOfNumber(2,3,4))

print(addSetOfNumber(2,3,4,5))


# ---------------------------------------------------------------------------------------------------------------------
# Part 02 : Simple use of *kwargs
# ---------------------------------------------------------------------------------------------------------------------

def printFullName (**namesInAnyOrder):

    for key, value in namesInAnyOrder.items():
        print ("%s = %s" %(key, value))
        if key == 'firstName':
            sFirstName = value
        elif key == 'lastName':
            sLastName = value

    return sFirstName + ' ' + sLastName

print('\nFull Name is : ' + printFullName(lastName = 'Gaadhe', firstName = 'Sandeep'))

# ---------------------------------------------------------------------------------------------------------------------
# Part 03 : Usage of args and kwargs for a fixed parametrized function
# ---------------------------------------------------------------------------------------------------------------------

def myFunc(arg1, arg2, arg3):
    print('\n')
    print('arg1 is ' + arg1)
    print('arg2 is ' + arg2)
    print('arg3 is ' + arg3)


args = ('value1', 'value2', 'value3')
myFunc(*args)

kwargs = {"arg3" : "value30", "arg1" : "value10", "arg2" : "value20"}
myFunc(**kwargs)














