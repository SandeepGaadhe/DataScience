import numpy as geek 
  
# 1D array with +ve integers 
array1 = [[1, 6, 1, 1, 1, 2, 2], [1, 6], [2, 3, 9], [2, 4, 6, 8]]


for i in range(len(array1)):
    print(array1[i])
    bin = geek.bincount(array1[i]) 
    print("Bincount output  : \n ", bin)
    print("size of bin : ", len(bin), "\n") 