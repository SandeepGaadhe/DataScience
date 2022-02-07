# -*- coding: utf-8 -*-

"""
Created on Wed Jan 15 14:53:59 2020

@author: admin
"""

#!/bin/python3

import sys
import os
import io
import re



# Complete the function below.
def subst(pattern, replace_str, string):
    #susbstitute pattern and return it
    #return string.replace(' ROAD ', ' RD.')
    i = pattern
    j = replace_str
    return re.sub(r'\b%s\b' %i,j, string)


def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
    #Create pattern Implementation here 
    new_address = [subst('ROAD', 'RD.', address) for address in addr]
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address

    return new_address

'''For testing the code, no input is required'''

if __name__ == "__main__":