# Consider the following independent samples s1 and s2:
# The samples represent the life satisfaction score (computed through a methodology) of older adults and younger adults respectively.
s1 = [45, 38, 52, 48, 25, 39, 51, 46, 55, 46]
s2 = [34, 22, 15, 27, 37, 41, 24, 19, 26, 36]

# Compute t-statistic for the above two groups, and display the t-score and p value in separate lines.
# Hint: Use the ttest_ind function available in scipy.

# Source : https://towardsdatascience.com/inferential-statistics-series-t-test-using-numpy-2718f8f9bf2f

## Import the packages
import numpy as np
from scipy import stats


## Define 2 random distributions

#Sample Size
N = 10 # possibly lenght of s1 or s2

#Gaussian distributed data with mean = 2 and var = 1
a = np.array(s1) # s1 #np.random.randn(N) + 2
#Gaussian distributed data with with mean = 0 and var = 1
b = np.array(s2) # s2 # np.random.randn(N)


## Calculate the Standard Deviation
#Calculate the variance to get the standard deviation

#For unbiased max likelihood estimate we have to divide the var by N-1, and therefore the parameter ddof = 1
var_a = a.var(ddof=1)
var_b = b.var(ddof=1)

#std deviation
s = np.sqrt((var_a + var_b)/2)
s



## Calculate the t-statistics
t = (a.mean() - b.mean())/(s*np.sqrt(2/N))



## Compare with the critical t-value
#Degrees of freedom
df = 2*N - 2

#p-value after comparison with the t 
p = 1 - stats.t.cdf(t,df=df)


print("t = " + str(t))
print("p = " + str(2*p))
### You can see that after comparing the t statistic with the critical t value (computed internally) we get a good p value of 0.0005 
# and thus we reject the null hypothesis and thus it proves that the mean of the two distributions are different and statistically significant.


## Cross Checking with the internal scipy function
t2, p2 = stats.ttest_ind(a,b)
print("t = " + str(t2))
print("p = " + str(p2))