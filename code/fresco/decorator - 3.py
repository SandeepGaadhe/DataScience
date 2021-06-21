def bold_tag(pFunc):
    def mClosure(*args, **kwargs):

        return '<b>' + args[0] + '</b>'
        # let's execute the real function and store the result
        #yourFuncRetValue = pFunc(*args, **kwargs)

        #let's print the returned value
        #print(f'LogMessage : Function {pFunc.__name__}() returned {yourFuncRetValue}')
        #return yourFuncRetValue
    return mClosure

@bold_tag
def say(msg):
    return msg

print (say('Decorator exercise'))
