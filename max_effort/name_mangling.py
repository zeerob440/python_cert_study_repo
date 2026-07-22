
class Name():
    def __init__(self, name):
        # name mangled 
        self.__name = name 

obj1 = Name('mia')

try:
    # cannot access name mangled var outside of class
    print(obj1.__name)
except AttributeError:
    print('AttributeError excepted\n')
    # because Python renames it _ClassName__varname
    print(obj1._Name__name)
