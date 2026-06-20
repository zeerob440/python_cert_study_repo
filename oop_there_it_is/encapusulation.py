# How Encapsulation works
# Methods and attributes whose names begin with __ are NAME-MANGLED
# and are intended for use only within the class. They are difficult,
# but not impossible, to access from outside the class.

# standard class declaration
class Soldier:
    def __init__(self, rank, lname):
        self.rank = rank
        self.lname = lname
# standard class recall 
rifleman = Soldier('pvt', 'James')
machine_gunner = Soldier('spc', 'Jenkins')

print(rifleman.rank)
print(rifleman.lname)

# encapsulation
class SpcOps:
    # declare attributes normally (self, specialty, name)
    def __init__(self, specialty, name):
        # place '__' on the left side of each 'attribute declaration' assignment statement
        self.__specialty = specialty
        self.__name = name
    
    def report(self):
        return f'{self.__specialty}: {self.__name}'

hmss = SpcOps('diver', 'bond')
n7 =SpcOps('SPECTER', 'shepard')  


#print(f'{hmss.specialty}:{hmss.name}')
# raises an AttrubuteError, because __name makes it difficult to reach outside the class.

# name and specialty are only easily reachable from the report function, but not easily reached
# by calling the 'name' or 'specialty' attributes. 
dossier = (hmss.report())

print(dossier)

# declaring a subclass and inheritance. 
# class SubClassName(SuperClassName)
class BlackOps(Soldier):
    # add all super class attributes, and add new subclass attributes anywhere
    def __init__(self, handler, rank, lname):
        # initiate Superclass next
        Soldier.__init__(self, rank, lname)

        # initiate the rest of the Subclass
        # this example uses name mangling because it is a black ops soldier
        self.__handler = handler
    
    def blackOpsDeadDrop(self):
        return f'{self.__handler}, {self.rank}, {self.lname}'

agent = BlackOps('diana', '***', '47')

leak =(agent.blackOpsDeadDrop())

print(leak)

# returns contents of a class instance
print(hmss.__dict__)

