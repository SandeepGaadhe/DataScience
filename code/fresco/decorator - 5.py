# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:47:49 2020

@author: admin
"""

import os
import sys

def bold_tag(func):
    
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'
        
    return inner

def italic_tag(func):
    
    def inner(*args, **kwdargs):
        return '<i>'+func(*args, **kwdargs)+'</i>'
        
    return inner
    
#Add greet() function definition
@italic_tag
def greet():
    return 'Hello World! Welcome to Python Programming Language'    

'''Check the Tail section for input/output'''

if __name__ == "__main__":