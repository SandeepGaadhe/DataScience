
def fib_gen():
    a,b=0,1
    print(f"a : {a} b : {b}")
    while a<4:
        yield a
        a,b=b,a+b

# The first two values of fibonacci series are 0, and 1.
# Create a generator fs from fib_gen function.
fs=fib_gen()

# Call next method on fs and print the returned value.
print(next(fs))

# Repeat the above step 3 more times, and display each returned value in a separate line.
print(next(fs))
print(next(fs))
print(next(fs))