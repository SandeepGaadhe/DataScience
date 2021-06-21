"""
Created on Thu Dec 12 15:30:12 2019

@author: admin
"""

# ------------------------------------------------------------------------------------
# Section 01 : Mean, Mode, Median : Not implemented completly
# ------------------------------------------------------------------------------------

import mDataSet as ms

# --------------------------------------
# Section 1.1 : Plotting Histogram
# --------------------------------------

from matplotlib import pyplot as plt

plt.bar(ms.xs, ms.ys)
plt.axis([0, 10, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()
