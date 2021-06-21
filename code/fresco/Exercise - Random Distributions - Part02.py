import numpy as np

#Create a normal distribution with mean 32 and standard deviation 4.5.
mu, sigma = 32, 4.5

#Set the random seed to 1, and create a random sample of 100 elements from the above defined distribution.
np.random.seed(1)
s = np.random.normal(mu, sigma, 100)


#Compute the absolute difference between the sample mean and the distribution mean.
print(abs(mu - np.mean(s)))
