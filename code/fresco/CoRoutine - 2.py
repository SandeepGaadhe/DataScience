
# Define 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
    
# Define coroutine 'linear_equation' as specified in previous exercise
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        retVal = 3*(x**2) + b
        print('Expression, '+str(a)+'*x^2 + '+str(b)+', with x being '+str(x)+' equals '+str(retVal))
          
