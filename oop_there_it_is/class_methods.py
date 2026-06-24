''' 
function hasattr() checks to see if a class OR object has a specified attribute
it returns a bool

'''

class AClass:
    def __init__(self, val):
        if val == 2:
            self.this = 'this attribute exists'
        else:
            self.that = 'this attribute does not exist'
        self.attr = 1 

output = AClass(2)

'''
since AClass attribute self.this exists since val = 2,
attribute self.that cannot exist so hasattr() returns False
'''
print(hasattr(output, 'this')) # True

print(hasattr(output, 'that')) # False

# hasattr() also works on classes

print(hasattr(output, 'attr')) # True
print(hasattr(output, 'ghost')) # False

print()
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2
 
 
example_object = ExampleClass()
 
print(hasattr(example_object, 'b')) # True because b is a local instance attribute under the class
print(hasattr(example_object, 'a')) # True because a is a global class attr
print(hasattr(ExampleClass, 'b')) # False because  b only exists on instances.
print(hasattr(ExampleClass, 'a')) # True because a is a global class attr