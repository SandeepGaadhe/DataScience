import collections
import mDataSet as ms
import math
import x_decorators as dec

@dec.mLog4p
def mean(x): # sensitive to outliers
    return sum(x) / len(x)

@dec.mLog4p
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
@dec.mLog4p
def mode(x):
    """returns a list, might be more than one mode"""
    counts = collections.Counter(x)
    # print(f"counts : {counts}")
    max_count = max(counts.values())
    # print(f"max_count : {max_count}")
    return ([x_i for x_i, count in counts.items()
            if count == max_count])

@dec.mLog4p
def quantile(x, p):
    """returns the pth-percentile value in x"""
    print(f"x : {x} p : {p} int(p * len(x)) : {int(p * len(x))}")
    p_index = int(p * len(x))
    print(f"p_index : {p_index}")
    print(f"x : {x}")
    print(f"sorted(x) : {sorted(x)}")
    print(f"sorted(x)[p_index] : {sorted(x)[p_index]}")
    return sorted(x)[p_index]

# dispersion : how is the spread of data
@dec.mLog4p
def data_range(x):
    print(f"x : {x}")
    print(f"max(x) : {max(x)}")
    print(f"min(x) : {min(x)}")
    return max(x) - min(x)

@dec.mLog4p
def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    print(f"x : {x}")
    print(f"x_bar : {x_bar}")
    return [x_i - x_bar for x_i in x]

@dec.mLog4p
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

@dec.mLog4p
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

@dec.mLog4p
def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
    variance(ms.num_friends)



"""
    Standard Deviation
    The square root of the variance is the standard deviation. 
    While var. gives you a rough idea of spread, 
    the standard deviation is more concrete, 
    giving you exact distances from the mean.
"""
@dec.mLog4p
def standard_deviation(x):
    from math import sqrt as sqaureroot
    return sqaureroot(variance(x))

# both mean and std deviation are very sensitive to outliers
# one of the robust way to handle outlier is to strip them out
# below example strips out 25th percentile and 75th percentile of data
# which possibly contains outliers
@dec.mLog4p
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

@dec.mLog4p
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

@dec.mLog4p
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero


def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

@dec.mLog4p
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0 # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1 # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 # consider the midpoint
        mid_p = normal_cdf(mid_z) # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

print ('\n\n------ End of ii_statisticsFunctions.py ------\n\n')















