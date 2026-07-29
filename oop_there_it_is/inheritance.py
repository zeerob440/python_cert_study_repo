
class Soldier():
    pass
# how to declare a subclass of a class class SuperClassHere(subClassHere)
# class inheritance can be daisy chained in this manner. 
class NCO(Soldier):
    pass
class Sergeant(NCO):
    pass

# issubclass(class1Here, class2Here)
# it is read literally is NCO a subclass of soldier (TRUE)
# is NCO a Subclass of Sergeant, (False), it is a subclass of NCO
print(issubclass(NCO, Soldier))
print(issubclass(NCO, Sergeant))
# is a subclass of Soldier because Sergeant is a subclass of NCO. NCO is a subclass of Soldier, and therefore inherits its properties
print(issubclass(Sergeant, Soldier))

jenkins_obj = Sergeant()
johnson_obj = Sergeant()
bishop_obj = Soldier()
bishop_android = bishop_obj # to demonstrate is operator determines if two vars are the same object/instance

# read literally again is object/instance , a Sergeant
print (isinstance(jenkins_obj, Sergeant))

# the is operator is used for comparison between two objects, it compares if the object-instance lives in the same memory address

print(bishop_obj is bishop_android) # returns True

print(Soldier is NCO)

# initiating a subclass with SuperClassName.__init__(self, name)

'''
SINGLE INHERITANCE - when on sub class inherits attributes for one super class

Python will always search and return the most specific class attribute
in my example below SuperClass __str__() command should return 'SuperClass'

but since instance-object toby is a SubClass it returns SubClass __str__() command

'''

class SuperClass():
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def __str__(self):
        return 'SuperClass.'
    
class UberClass():
    def __init__(self, color):

        self.color = color

class SubClass(SuperClass):
    def __init__(self, name, ability, number):
        self.number = number
        SuperClass.__init__(self, name, ability)

    def __str__(self):
        return "Subclass."

toby = SubClass('Toby', 'Jumping', 13)

print(toby)
print(isinstance(toby, SubClass)) # True
print(isinstance(toby, SuperClass)) # True

# multi inheritance ClassName(SuperClassOne, SuperClassTwo)
class SuperUberSubClass(UberClass, SuperClass):
    def __init__(self, name, ability, color ):

# super classes must be constructed inside subclasses to be used. 
        SuperClass.__init__(self, name, ability)

        UberClass.__init__(self, color)

    def __str__(self):
        return "I'm a superubersubclass."
    
super_uber_obj = SuperUberSubClass('charles', 'flying', 'red')

print(super_uber_obj)

        
         
