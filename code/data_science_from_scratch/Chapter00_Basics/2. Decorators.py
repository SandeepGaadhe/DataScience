# -*- coding: utf-8 -*-
"""

Created on Fri Dec  6 11:18:05 2019

@author: admin

@source : https://dbader.org/blog/python-decorators

@description : The script explains the use case of decorators.
"""

# ---------------------------------------------------------------------------------------------------------------------
# Part 01 : Simple use case of decorator
# ---------------------------------------------------------------------------------------------------------------------

print('\n---------------------------------------------------------------------------------------------------------------------'
      '\n *** Part 01 : Simple use case of decorator ***'
      '\n---------------------------------------------------------------------------------------------------------------------'
      )

# this is a simple function whose behaviour will be changed
# later using a decorator
def greet():
    return 'Hello!'

print(greet())

# let's now define a decorator which can be used to change
# the definition of greet() which actually changing any
# code inside it

# In basic terms, a decorator is a callable that takes a callable
# as input and returns another callable.

# this resonates the factor example under FuncationAsObject.py
def decUpperCase(anyFunc):

    # this is the closure function
    def mClosureFunc():
        passedFunc = anyFunc()
        modifiedBehaviour = passedFunc.upper()
        return modifiedBehaviour
    return mClosureFunc


# let's use the decorator now

print('Before applying decorator : ' + greet())

@decUpperCase
def greet():
    return 'Hello!'

print('After applying decorator : ' + greet())

print('Second run after applying decorator : ' + greet())

# ---------------------------------------------------------------------------------------------------------------------
# Part 02 : Applying multiple decorators
# ---------------------------------------------------------------------------------------------------------------------

print('\n---------------------------------------------------------------------------------------------------------------------'
      '\n *** Part 02 : Applying multiple decorators ***'
      '\n---------------------------------------------------------------------------------------------------------------------'
      )


def makeBold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def makeItalic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper


# do note that as soon as new decorator is applied
# the previous decorator is washed out

# also note that the decorator is always applied
# bottom to top

@makeBold
@makeItalic
def greet():
    return 'Hello!'

print('After applying decorator : ' + greet())

# ---------------------------------------------------------------------------------------------------------------------
# Part 03 : Decorating functions that accept arguments
# ---------------------------------------------------------------------------------------------------------------------

print('\n---------------------------------------------------------------------------------------------------------------------'
      '\n *** Part 03 : Decorating functions that accept arguments ***'
      '\n---------------------------------------------------------------------------------------------------------------------'
      )

# to read more about f' string (formatted string literals)
# https://realpython.com/python-f-strings/

# below is a simple function which do not have tracer
def say(name, message):
    return f'Hello {name} : {message}'



print('\n')
print(say('Sandeep', 'Be a Data Scientist!!!'))

# let's define a logger decorator

def mLog4p(pFunc):
    def mClosure(*args, **kwargs):

        # first print the function that is called and what parameter is passed
        print(f'LogMessage : Called {pFunc.__name__}() with varargs as {args} and kwargs as {kwargs}')

        # let's execute the real function and store the result
        yourFuncRetValue = pFunc(*args, **kwargs)

        #let's print the returned value
        print(f'LogMessage : Function {pFunc.__name__}() returned {yourFuncRetValue}')
        return yourFuncRetValue
    return mClosure

# now let's add our logger to say() function
@mLog4p
def say(name, message):
    return f'Hello {name} : {message}'

print('\n')
print(say('Sandeep', 'Great Job by adding a tracer!!!'))

# ---------------------------------------------------------------------------------------------------------------------
# Part 04 : Debugging Decorators
# ---------------------------------------------------------------------------------------------------------------------

print('\n---------------------------------------------------------------------------------------------------------------------'
      '\n *** Part 04 : Debugging Decorators ***'
      '\n---------------------------------------------------------------------------------------------------------------------'
      )

def greet():
    """DocString inside greet()"""
    return 'Hello!'

# utility function to handle none - nothing to do with debugging decorator
def mHandleNoneType(s):
    if s is None:
        return 'mNoneType'
    else:
        return s

decorated_greet = decUpperCase(greet)


# observe that both name and docstring is well printed for first-class greet() function
print('Calling greet() : ' + greet() + ' . greet__name__ : ' + greet.__name__  + ' . greet__doc__ : ' + greet.__doc__)


# observe that for a decorated function, the closure function name is printed with no doc string
# which makes it difficult to debug
print(
      'Calling decorated_greet() : ' + decorated_greet() + ' . decorated_greet__name__ : '
      + decorated_greet.__name__  + ' .  decorated_greet__doc__ : ' +   mHandleNoneType( decorated_greet.__doc__)
      )

import functools

def debuggableDecUpperCase(anyFunc):
    @functools.wraps(anyFunc)
    def mClosureFunc():
        passedFunc = anyFunc()
        modifiedBehaviour = passedFunc.upper()
        return modifiedBehaviour
    return mClosureFunc

# let's re-assign debuggable decorator to decorated_greet
decorated_greet = debuggableDecUpperCase(greet)


# observe that now for a decorated function as well, the closure function name and its doc string
# is printed
print(
      'Debuggable : Calling decorated_greet() : ' + decorated_greet() + ' . decorated_greet__name__ : '
      + decorated_greet.__name__  + ' .  decorated_greet__doc__ : ' +   mHandleNoneType( decorated_greet.__doc__)
      )
