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
    
#Add greet() implementation here
@italic_tag
@bold_tag
def greet():
    return input()

'''check Tail section below for input / output'''

if __name__ == "__main__":