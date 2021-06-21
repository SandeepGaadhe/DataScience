
import ii_statisticsFunctions as sf

#print(sf.mean(sf.ms.num_friends))

#print(sf.median(sf.ms.num_friends))

#print(sf.mode(sf.ms.num_friends))

#print(sf.quantile(sf.ms.num_friends,0.25))

#print(sf.data_range(sf.ms.num_friends))

#print(sf.de_mean(sf.ms.num_friends))

# remember : variance does the squaring first
# to negate the effect of negative-positive sum
#print(sf.variance(sf.ms.num_friends))

# ----------------------------------------
# Understand Std Deviation
# ----------------------------------------

# std deviation is just a sqrt of deviation
# to get the result in more understandable units
# friends-squered (variance) --> friends (std dev)

# Ten 2's and Ten 1's
num_friends = [2 , 2 ,  2 ,  2 ,  2 ,  2 ,  2 ,  2 ,  2 ,  2 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ]
print(sf.mean(num_friends)) # 1.5
print(sf.standard_deviation(num_friends)) # 0.51

# above, mean returned 1.5 and sd is 0.51 which is inline with data set

num_friends = [1 , 4 , 4 , 3 , 2 , 2 , 4 , 4 , 1 , 1 , 1 , 3 , 3 , 1 , 4 , 4 , 0 , 3 , 1 , 2]
#print(sf.standard_deviation(num_friends)) # 1.35

num_friends = [1 , 1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ]
#print(sf.standard_deviation(num_friends)) # 0.00


num_friends = [100 , 1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ]
#print(sf.standard_deviation(num_friends)) # 22.13




