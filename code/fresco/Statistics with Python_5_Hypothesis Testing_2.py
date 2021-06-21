# A researcher noted the number of chocolate chips consumed by 10 rats, with and without electrical stimulation.
# The data set s1 represents consumption with stimulation, and s2 without simulation.
s1 = [12, 7, 3, 11, 8, 5, 14, 7, 9, 10]
s2 = [8, 7, 4, 14, 6, 7, 12, 5, 5, 8]

# Compute t-statistic for the above samples, and display the t-score and p-value in separate lines.
# Hint: Use the ttest_rel function available in scipy.
import numpy as np
from scipy import stats

a = np.array(s1) 
b = np.array(s2) 

## Checking with the internal scipy function
t2, p2 = stats.ttest_rel(a,b)
print("t = " + str(t2))
print("p = " + str(p2))

