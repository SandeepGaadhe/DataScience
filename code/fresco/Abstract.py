import inspect


from abc import ABC, abstractmethod

# Define the abstract class 'Animal' below
# with abstract method 'say'
class Animal:
    @abstractmethod
    def say(self):
        pass

# Define class Dog derived from Animal
# Also define 'say' method inside 'Dog' class
class Dog(Animal):
    def say(self):
        return 'I speak Booooo'

print("'Animal' is an abstract class")
d1 = Dog()
d1.say()