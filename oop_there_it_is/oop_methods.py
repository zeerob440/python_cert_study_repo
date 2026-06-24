# OOP Methods


class Dog:
    # a METHOD is a function inside a class
    # self is n
    def bark(self): # this is a METHOD
        print("Woof!")

dog1 = Dog() # creates a Dog object in memory

dog1.bark() # calls method, prints 'Woof!'
# python in the back does Dog.bark(dog1)

# so SELF is the object called me. (specific class instance)
