"""
Created on Thu Dec 12 15:30:12 2019

@author: admin
"""

# ------------------------------------------------------------------------------------
# Section 01 : Mean, Mode, Median : Not implemented completly
# ------------------------------------------------------------------------------------

import collections
import sys


# random list generated using https://www.random.org/ for 0 to 4
num_friends = [1 , 4 , 4 , 3 , 2 , 2 , 4 , 4 , 1 , 1 , 1 , 3 , 3 , 1 , 4 , 4 , 0 , 3 , 1 , 2]
print(f"num_friends : {num_friends}")

friend_counts = collections.Counter(num_friends)
print(f"friend_counts : {sorted(friend_counts.items())}")
xs = range(5)
ys = [friend_counts[x] for x in xs] # height is just # of friends

for x in xs:
    print(f"x : {x} has {ys[x]} friends")


# --------------------------------------
# Section 1.1 : Plotting Histogram
# --------------------------------------

from matplotlib import pyplot as plt

plt.bar(xs, ys)
plt.axis([0, 10, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

# -----------------------------------------------
# Section 1.2 : Know Central Tendencies by Mean, Median, Mode
# -----------------------------------------------

num_points = len(num_friends) # 20

print(f"num_points : {num_points}")

has_max_friends = max(num_friends)
has_least_friends = min(num_friends)

print(f"has_max_friends : {has_max_friends} has_least_friends : {has_least_friends}")

def mean(x): # sensitive to outliers
    return sum(x) / len(x)

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
    # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

# most common/repeating value
def mode(x):
    """returns a list, might be more than one mode"""
    counts = collections.Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]

# -----------------------------------------------
# Section 1.2 : Know Central Tendencies by Mean, Median, Mode
# -----------------------------------------------

def quantile(x, p):
    """returns the pth-percentile value in x"""
    print(f"x : {x} p : {p} int(p * len(x)) : {int(p * len(x))}")
    p_index = int(p * len(x))
    return sorted(x)[p_index]

q_tenth = quantile(num_friends, 0.30)

print(f"quantile(num_friends, 0.10) : {q_tenth}")

print(sorted(num_friends)[12])

# dispersion : how is the spread of data
def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

"""
The variance for a population is calculated by:

1.  Finding the mean(the average).

2.  Subtracting the mean from each number in the data set and then squaring the result. 
    The results are squared to make the negatives positive. Otherwise negative numbers 
    would cancel out the positives in the next step. 
    It’s the distance from the mean that’s important, not positive or negative numbers.

3.  Averaging the squared differences.

"""

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
    variance(num_friends)



"""
    Standard Deviation
    The square root of the variance is the standard deviation. 
    While var. gives you a rough idea of spread, 
    the standard deviation is more concrete, 
    giving you exact distances from the mean.
"""
def standard_deviation(x):
    from math import sqrt as sqaureroot
    return sqaureroot(variance(x))

# both mean and std deviation are very sensitive to outliers
# one of the robust way to handle outlier is to strip them out
# below example strips out 25th percentile and 75th percentile of data
# which possibly contains outliers
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

# START WITH CORRELATION PAGE 103
















