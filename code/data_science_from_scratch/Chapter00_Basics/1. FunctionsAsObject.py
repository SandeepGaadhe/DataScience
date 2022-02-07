# -*- coding: utf-8 -*-


"""

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

Created on Thu Dec  5 16:14:09 2019

@author: admin

@source : https://dbader.org/blog/python-first-class-functions

@description :  this script to demostrate the usage of functions as object.
                the importance of concept is that in below example, you will 
                find functions like yell, bark, polite etc. A generic function
                greet is defined and greet accepts function (like yell, bark, polite)
                as argument. The point is behaviour of greet changes as per the
                function argument that is passed.
                Now, the simple solution in traditional approach is to pass a 
                string parameter, that defines whether to yell or bark or polite 
                and then call the necessary function. 
                
                Not 100% clear, what the real benefit of passing func as argument.
                
                Possibly, helping in having a Factory patter(see make_adder)


----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
"""

sMessage = 'i aM pYtHoN PrOgRaMmEr'

def yell(sText):
    return '\n' + sText.upper() + '!!!'

def polite(sText):
    return '\n Hello.' + str.capitalize(sText) + '!!!'



print(yell('yell : ' + sMessage))

bark = yell

print('\n' + bark('bark : ' + sMessage))

# internally bark name is stored as yell only
print('bark.__name__ : ' + bark.__name__)


print('\n' + polite('polite : ' + sMessage))


#storing functions as data structure

lFunctions = [bark, str.lower, str.capitalize]

print(lFunctions)

#calling the functions stored in list data structures

#calling bark

print(lFunctions[0]("calling function stored inside list"))

#calling str.lower
print(lFunctions[1]("CONVERT ME TO LOWER USING STORED FUNCTION IN LIST"))

#calling str.Capitalize
print(lFunctions[2]("convert me to capitalize using stored function in list"))


# Passing function as argument
def greet(pAnyFunc, sAnyFuncName):
    
    print('\n\nInside greet : ' + pAnyFunc.__name__)
    print('sAnyFuncName : ' + sAnyFuncName)
    
    if pAnyFunc.__name__ == 'yell':
        sGreet = 'Yell : ' + pAnyFunc(sMessage)
    elif pAnyFunc.__name__ == 'bark':
        sGreet = 'Bark : ' + pAnyFunc(sMessage)
    print(sGreet)
    
greet(yell, 'passed param function name is yell')
greet(bark, 'passed param function name is bark')


# create an adder function that creates another function
# that will add the number automatically

def make_adder(iAdderNumber):
    
    # create a function that will set the iAdderNumber
    # as permanant object specific behavior
    def yourAdderFunc(iAnyNumber):
        return iAnyNumber + iAdderNumber
    return yourAdderFunc

# Now let us the factory function make_adder that
# will create use as many function as we want
    
myPlus3Func = make_adder(3)
myPlus5Func = make_adder(5)
myPlus7Func = make_adder(7)

iTestValue = 20

print('\n\niTestValue : ' + str(iTestValue))

iRetValue = myPlus3Func(iTestValue)
print('iRetValue using myPlus3Func : ' + str(iRetValue))

iRetValue = myPlus5Func(iTestValue)
print('iRetValue using myPlus5Func : ' + str(iRetValue))

iRetValue = myPlus7Func(iTestValue)
print('iRetValue using myPlus7Func : ' + str(iRetValue))
























