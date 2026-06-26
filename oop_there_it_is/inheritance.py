
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
# is a subclass of Soldier because Sergeant is a subclass of NCO. NCO is a subclass of Soldier, and there for inherits its properties
print(issubclass(Sergeant, Soldier))

jenkins_obj = Sergeant()

# read literally again is object/instance , a Sergeant
print (isinstance(jenkins_obj, Sergeant))