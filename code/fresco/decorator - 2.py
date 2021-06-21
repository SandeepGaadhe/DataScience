#!/bin/python3

import sys
import os



def log(func):
    def inner(*args, **kwdargs):
        str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__,
                                                                                args,
                                                                                kwdargs)
        return str_template + "\n" + str(func(*args, **kwdargs))
    return inner

#Add greet function definition here

@log
def average(n1,n2,n3):
    return (n1+n2+n3)/3


'''Check the Tail section for input/output'''

if __name__ == "__main__":