# Define the generator function factorial_gen, which is capable of yielding factorial values of natural numbers.
def factorial_gen():
    a = 0
    while True:
        if a == 0:
            a = 1
            yield a
            lastYield = a
        else:
            yield lastYield * a
            lastYield = lastYield * a
            a += 1
 
# Create a generator fs from factorial_gen.
fs=factorial_gen()
# Ensure, the first two values to be yielded by fs are 1 and 1, corresponding to factorial of 0 and 1 respectively.
# Call next method on fs and print the returned value.
print(next(fs))
# Repeat the above step 3 more times, and display each returned value in a separate line.
print(next(fs))
print(next(fs))
print(next(fs))
