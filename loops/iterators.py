'''iterable classes must have __iter__() and __next__().
The for loop is repeatedly calling __next__() until StopIteration is raised.
'''

class ThreeNums:
    def __init__(self):
        self.number = 1
        # __iter__ tells Python that this object-instance is iterable.
        # if __iter__is used it MUST be paired with __next__
        # __iter__ declares to python the object_instance is iterable
        # __next__ tells python what the value of that iteration is.
    def __iter__(self):
        return self
    # __next__ is where StopIteration needs to be raised. 
    def __next__(self):
        if self.number > 3:
            raise StopIteration

        value = self.number
        self.number += 1

        return value
# x is instance-object 
x = ThreeNums()

for i in ThreeNums():
    print (i)

print('yield\n')
'''
yield

yield is one of the most abstract Python concepts.

Purpose:
• Creates a generator.
• A generator produces one value at a time instead of all values at once.

Rules:
1. yield only appears inside a function.
2. Calling that function returns a generator object (not the values).
3. next(generator) requests the next value.
4. A for loop automatically calls next() repeatedly.
5. The function pauses after each yield and resumes at the next next() call.
6. When the function ends, StopIteration is raised automatically.

Common use cases:
• Infinite sequences
• Reading very large files
• Streaming data
'''

import random
# yield alway lives in a function
def dice():
    while True:
        # only returns random ints between 1-6 once per call
        yield random.randint(1, 6)

# object-instance needs to exist to function usefully.
g = dice()
# must be used with next() to function in a useful manner. 
print(next(g))
print(next(g))



