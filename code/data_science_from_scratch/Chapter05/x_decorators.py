def mLog4p(pFunc):
    def mClosure(*args, **kwargs):

        print("\n\n-------------------------------------------------------------")
        # first print the function that is called and what parameter is passed
        print(f'LogMessage : Called {pFunc.__name__}() with varargs as {args}') # and kwargs as {kwargs}')

        # let's execute the real function and store the result
        yourFuncRetValue = pFunc(*args, **kwargs)

        #let's print the returned value
        print(f'LogMessage : Function {pFunc.__name__}() returned {yourFuncRetValue}')
        print("-------------------------------------------------------------")
        return yourFuncRetValue
    return mClosure
