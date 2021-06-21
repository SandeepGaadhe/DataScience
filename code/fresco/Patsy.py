# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:11:28 2020

@author: admin
"""

import numpy as np

y = np.array([1, 2, 3, 4, 5])
x1 = np.array([6, 7, 8, 9, 10])
x2 = np.array([11, 12, 13, 14, 15])

# create of 1d array of 5 elements of 1
print(np.ones(5))

# this means stack the arrays vertically, e.g. on top of each other
X = np.vstack([np.ones(5), x1, x2, x1*x2]).T

print(f'y without using Patsy : {y}')
print(f'X without using Patsy : {X}')

print('\n\n--------------------------------------------\n\n')

# Rewriting same example with Patsy
import patsy

data = {'y':y, 'x1':x1, 'x2':x2}

print(f'data : {data}')


# Let's understand few patsy formulae provided below.
# 'y ~ x' : y is linearly dependent on x. ~ symbol separates dependent variable from independent variable terms. It is also equivalent to 'y ~ 1 + x'.
# 'y ~ x1 + x2' : y is a linear combination of x1 and x2. + sign is used to denote the union of terms.
# y ~ x1*x2 : x1*x2 is an interaction term that includes all lower order terms. Hence formula is equivalent to y ~ 1 + x1 + x2 + x1*x2.
y, X = patsy.dmatrices('y ~ 1 + x1 + x2 + x1*x2', data)

print(f'y using Patsy : {y}')
print(f'X using Patsy : {X}')