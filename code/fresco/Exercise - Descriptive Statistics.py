
from scipy import stats as st
import numpy as np

s = [26, 15, 8, 44, 26, 13, 38, 24, 17, 29]
# s = [15,5]

#Mean,
s1 = np.array(s)
print(np.mean(s1))
#Median,
print(np.median(s1))
#Mode,
print(st.mode(s1))

#25th and 75th percentile,
print(np.percentile(s1, [25, 75], interpolation='lower'))
#print(np.percentile(s1, 25)) #, interpolation='lower'))
#print(np.percentile(s1, 75)) #, interpolation='lower'))
#Inter quartile range,
print(st.iqr(s1, rng=(25,75), interpolation='lower'))

#Skewness,
print(st.skew(s1))
#Kurtosis.
print(st.kurtosis(s1))