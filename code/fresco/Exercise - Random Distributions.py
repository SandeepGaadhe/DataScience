import scipy as sp
from scipy import stats
import numpy as np

n, p = 1, .5  # number of trials, probability of each trial
np.random.seed(1)
s = np.random.binomial(n, p, 10000)

print(s)
k = np.bincount(s)


print(k[0])
print(k[1])
#print(k.count(1))