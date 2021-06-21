print('Step 0')
def coroutine_decorator(func):
    print(f'inside coroutine_decorator {func}')
    def wrapper(*args, **kwdargs):
        print(f'LogMessage : Called {func.__name__}() with varargs as {args} and kwargs as {kwdargs}')
        c = func(*args, **kwdargs)
        next(c)
        return c
    print(f'LogMessage : return wrapper {wrapper}')
    return wrapper


print('Step 0.1')
@coroutine_decorator
def TokenIssuer(tokenId=0):
    print('inside tokenissuer')
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)

print('step 1')
t = TokenIssuer(100)
print('step 2')
t.send('George')
print('step 3')
t.send('Rosy')
print('step 4')
t.send('Smith')
print('step 5')
t.close()
print('step 6')
