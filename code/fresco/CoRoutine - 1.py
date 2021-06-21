def linear_equation(a, b):
    while True:
        x = yield
        retVal = 3*(x**2) + b
        print("Expression, 3.0*x^2 + 4.0, with x being", x, "equals", retVal)
        

def myMain():
    a = float(input())

    b = float(input())
    equation1 = linear_equation(a, b)
    next(equation1)
    equation1.send(6)

myMain()