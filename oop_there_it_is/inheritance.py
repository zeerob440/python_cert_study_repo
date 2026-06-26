
class Soldier():
    pass
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