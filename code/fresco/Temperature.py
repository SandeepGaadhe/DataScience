#!/bin/python3

import sys
import os



# Add Celsius class implementation below.
class Celsius:

    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5
        

# Add temperature class implementation below.        
class Temperature:
    
    celcius = Celsius()
    
    def __init__(self, tempF):
        self.fahrenheit = int(tempF)

t1 = Temperature(int(input("Enter F")))
print(t1.fahrenheit)
print(t1.celcius)

t1.celcius = int(input("Enter C"))
print(t1.fahrenheit)
print(t1.celcius)


'''Check the Tail section for input/output'''
#
#if __name__ == "__main__":
#    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
#        res_lst = list()
#        t1 = Temperature(int(input()))
#        res_lst.append((t1.fahrenheit, t1.celsius))
#        t1.celsius = int(input())
#        res_lst.append((t1.fahrenheit, t1.celsius))
#        fout.write("{}\n{}".format(*res_lst))