"""
Created on Thu Dec 12 15:30:12 2019

@author: admin
"""

# ------------------------------------------------------------------------------------
# Section 01 : Mean, Mode, Median : Not implemented completly
# ------------------------------------------------------------------------------------

import collections

# random list generated using https://www.random.org/ for 0 to 4
num_friends = [1 , 4 , 4 , 3 , 2 , 2 , 4 , 4 , 1 , 1 , 1 , 3 , 3 , 1 , 4 , 4 , 0 , 3 , 1 , 2]
print(f"num_friends : {num_friends}")

friend_counts = collections.Counter(num_friends)
print(f"friend_counts : {sorted(friend_counts.items())}")
xs = range(5)
ys = [friend_counts[x] for x in xs] # height is just # of friends

for x in xs:
    print(f"x : {x} has {ys[x]} friends")

print(f"len(num_friends) : {len(num_friends)}")
print(f"max(num_friends) : {max(num_friends)}")
print(f"min(num_friends) : {min(num_friends)}")

print ('\n\n------ End of mStatistics.py ------\n\n')