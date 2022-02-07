#coroutine decorator    

def coroutine_decorator(coroutine_func):
    def wrapper(*args,**kwargs):
    c=coroutine_func(*args,**kwargs)
    next(c)
    return c
return wrapper

# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x=yield
        e=a*(x**2)+b
        print("Expression, {0}*x^2 + {1}, with x being {2} equals {3}".format(int(a),x,int(b),int(e)))

# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    while True :
        x = yield
        equation1.send(x)
        equation2.send(x)
    

print('step 0.3')
def main(x):
    print('inside main')
    n = numberParser()
    print('back to main')
    n.send(x)
    print('exiting main')
    
print('step 0.4')
def myMain():
    print("inside mymain enter float")
    x = float(input())
    res = main(x);

myMain()