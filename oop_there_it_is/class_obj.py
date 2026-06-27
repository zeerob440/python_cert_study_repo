# oop study guide

# declaring a class
# this class has no methods or attributes

class SimpleClass():
    pass

# declaring a class instance-object
first_obj = SimpleClass()

# __init__ is a constructor it must contain at least one parameter; self
# constructors are implicitly run
class Stack:
    def __init__(self):
        self.stack_list = []
        
# used dot notation to access a class's properties. 
stack_obj = Stack()
print(len(stack_obj.stack_list))


