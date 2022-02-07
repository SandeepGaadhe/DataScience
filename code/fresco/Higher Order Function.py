#!/bin/python3

import sys
import os

#Write detecter implementation
def detecter(element):
    #Write isIn implementation    
    def isIn(sequence):
        return True if element in sequence  else False
    return isIn


#Write closure function implementation for detect30 and detect45

detect30 = detecter(30)
detect45 = detecter(45)

detect30([2,30,45,6])

if __name__ == "__main__":