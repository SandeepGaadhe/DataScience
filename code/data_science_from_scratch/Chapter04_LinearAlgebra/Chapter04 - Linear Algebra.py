# -*- coding: utf-8 -*-

"""
Created on Wed Dec 11 13:29:53 2019

@author: admin
"""

# ----------------------------------------------------------------------------------------
# Section 01 : Vectors (One dimensional array/list)
# ----------------------------------------------------------------------------------------

v1 = [1,2]
v2 = [5,7]

print(f"v1 : {v1} v2 : {v2}")
for i,j in zip(v1, v2): print (f"Zip(v1, v2) : {i} {j}")

# ------------------------------------------
# Section 1.1 : def
# ------------------------------------------

def vectorAdd(pv1, pv2):
    return [i + j for i, j  in zip (pv1, pv2)]

def vector_subtract(pv1, pv2):
    return [i - j for i, j  in zip (pv1, pv2)]

from functools import reduce

def vectorsSum(vectors):
    return reduce(vectorAdd, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vectorsSum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

# ------------------------------------------
# Section 1.2 : def usage
# ------------------------------------------

print(f"vectorAdd(v1,v2) : {vectorAdd(v1,v2)}")

print(f"vector_subtract(v1,v2) : {vector_subtract(v1,v2)}")


l_vectors = [v1, v2]
print(f"vectorsSum(l_vectors) : {vectorsSum(l_vectors)}")


scalar_multiplyRes = scalar_multiply(3,v1)
print(f"scalar_multiplyRes by 3 : {scalar_multiplyRes}")


l_vectors = [v1, v2]
vectors_meanRes = vector_mean(l_vectors)
print(f"vectors_meanRes : {vectors_meanRes}")

dotRes = dot(v1,v2)
print(f"dotRes dot(v1,v2) : {dotRes}")


print(f"sum_of_squares(v1) : {sum_of_squares(v1)}")

print(f"magnitude(v1) : {magnitude(v1)}")

print(f"squared_distance(v1, v2) : {squared_distance(v1, v2)}")

print(f"distance(v1, v2) : {distance(v1, v2)}")


# ----------------------------------------------------------------------------------------
# Section 02 : Matrices : (Two dimensional array/list) : Not Implemented
# ----------------------------------------------------------------------------------------









