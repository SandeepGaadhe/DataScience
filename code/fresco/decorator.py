#!/bin/python3

import sys
import os
import datetime as dt

#Add log function and inner function implementation here
def log(pFunc):
    def mClosure(*args, **kwargs):

        # first print the function that is called and what parameter is passed
        logMsg = "Accessed the function -'" + pFunc.__name__ +"' with arguments ('" + args[0] + "',) {}"
        #print(logMsg) # and kwargs as {kwargs}')

        # let's execute the real function and store the result
        #yourFuncRetValue = pFunc(*args, **kwargs)

        #let's print the returned value
        #print(f'LogMessage : Function {pFunc.__name__}() returned {yourFuncRetValue}')
        #print("-------------------------------------------------------------")
        #return yourFuncRetValue
        return logMsg
    return mClosure

@log
def greet(msg):
    'Greeting Message : ' + msg

'''Check the Tail section for input/output'''