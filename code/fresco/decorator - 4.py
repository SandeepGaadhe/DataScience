# -*- coding: utf-8 -*-

"""
Created on Wed Jan 15 18:45:14 2020

@author: admin
"""

import os
import sys


def bold_tag(func):
    
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'
        
    return inner

#Implement italic_tag below
def italic_tag(func):
    
    def inner(*args, **kwdargs):
        return '<i>'+func(*args, **kwdargs)+'</i>'
        
    return inner

@italic_tag
def say(msg):
    return msg
    
'''Check the Tail section for input/output'''

if __name__ == "__main__":