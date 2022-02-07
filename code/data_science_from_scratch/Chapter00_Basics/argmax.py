# Python Program illustrating 
# working of argmax() 



import numpy as npa 



print('\n\n\n----------------------\nWorking on 1D array\n----------------------\n')
array = [10, 25, 40,30, 15]
print("INPUT ARRAY : \n", array) 

# using argmax
print("\nMax element npa.argmax(array) : ", npa.argmax(array)) 





print('\n\n\n----------------------\nWorking on 2D array\n----------------------\n')
array = [[10, 2500, 40,30, 15], [100,  400, 250, 300, 150]]
print("INPUT ARRAY : \n", array) 
print('\n')
for s in array:
    print(*s)
    #print(s)

# No axis mentioned, so works on entire array 
print("\nMax element npa.argmax(array) : ", npa.argmax(array)) 

# 10 100 --> 1, 2500 400 --> 0 40 250 --> 1 30 300 --> 1 15 150 --> 1
print("\nIndices of Max element npa.argmax(array, axis=0) Y axis : ", npa.argmax(array, axis=0)) 

# 10 2500 40 30 15 --> 1 100 400 250 300 150 --> 1
print("\nIndices of Max element npa.argmax(array, axis=1) X axis : ", npa.argmax(array, axis=1)) 
