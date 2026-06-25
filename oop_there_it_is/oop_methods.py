# OOP Methods


class Dog:
    # a METHOD is a function inside a class

    def bark(self): # this is a METHOD
        print("Woof!")

dog1 = Dog() # creates a Dog object in memory

dog1.bark() # calls method, prints 'Woof!'

methods: str ='''
Python in the back does Dog.bark(dog1)
so SELF is the object called. (specific class instance)
\n'''
print(methods)

self_att1: str ='''
SELF allows the method access the object/instance attributes
because self.name  means rico.name. so self.name means instance/object.name
\n'''

print(self_att1)
class Schnauzer:

    def __init__(self, name): # constructor __init__ builds instances
        self.name = name

    def bark(self): # method
        print(self.name, 'says woof\n')

rico = Schnauzer('Rico') # class instance/object

rico.bark()

self_note: str = '''
SELF can access both instance/object and class vars.
It returns object/instance var first then class vars\n'''

print(self_note)
class YukonWhalingShepard:
    species = 'Canine' # class variable
  
    def __init__(self, name): # method
        
        self.name = name  # instance variable

    def info(self): # method
        print(self.species, '\n')
        print(self.name, '\n')

mia = YukonWhalingShepard('Mia')

mia.info()

m_m: str ='''
Methods can call methods.\n'''

class Cat:


    def __init__ (self, name): # constructor
        self.name = name

    def meow(self): # method
        print('meow!\n')

    def hiss(self): # method
        print('Hiss!\n')
        self.meow() # method invoking method


moose = Cat('Moose') # object/Instance

moose.hiss()

## __init__ runs automatically for each instance after __init__ initially declared

