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
1. Look on the instance (object).
2. If not found, look on the class.
3. If still not found, AttributeError.\n'''

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

# __dict__ing around
'''
| Special Attribute | Belongs to                         | Meaning                           |
| ----------------- | ---------------------------------- | --------------------------------- |
| `__name__`        | **Class** (also functions/modules) | "What's your name?"               |
| `__base__`        | **Class**                          | "Who's your parent?"              |
| `__module__`      | **Class**                          | "Which Python file are you from?" |
| `__dict__`        | **Both**                           | "What do you contain?"            |
'''
# dict returns all the attributes of an instance if aimed at an instance object
print(moose.__dict__)
# if __dict__ is aimed at a class, it returns all the methods and attributes in the class and the memory location.
print(Cat.__dict__)

# __name__ returns name of class if aimed at class

print(Cat.__name__)

# __name__ does not work on objects/instances, returns AttributeError
#print(moose.__name__)
# __module returns where the class lives, works on methods, classes, instance objects
print(Cat.__module__)
print(Cat.hiss.__module__)
print(moose.__module__)

## __init__ runs automatically for each instance after __init__ initially declared


'''
__init__ is a method, and a method is a function, it can be treated as such
__init__ must have a self parameter
it is used to set up object instances

__init__ cannot return a value
__init__ cannot be directly invoked from the class or the object
'''
# methods can be invoked without arguments
# methods must be declared with at least parameter (self)

# inner life of class objects