import math
import random
import collections as c

import sys
sys.path.append("S:\SandeepG\Official\DataScience\Code\DataScienceFromScratch\Chapter05")
import ii_statisticsFunctions as sf

from matplotlib import pyplot as plt

def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    # remember, a counter is a container that keeps count of each item in list/dict
    return c.Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()
    
random.seed(0)

#uniform = [int(200 * random.random()) - 100 for _ in range(10)]
#print(f"uniform : {uniform}")

normal = [57 * sf.inverse_normal_cdf(random.random()) for _ in range(10)]
print(f"normal : {normal}")

plot_histogram(normal, 5, "Normal Histogram")