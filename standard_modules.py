import hashlib

import random as chaos
'''
dir()
dir() returns a list of entities within a module as seen below

'''
print('dir() is action below\n')
print()
contents = dir(hashlib)

print(contents)
print()
print('alias dir() example below\n')
# If a module has been imported with an alias dir(alias)
contents_content = dir(chaos)

print (contents_content)
'''
MATH MODULE NOTES
ENTITIES Within
TRIG
sin(x) sine of x
cos(x) cosine of x
tan(x) tangent of x
asin(x) arcsine x
acos(x) arccosine of x
atan(x) arctangent of x
RETURNS ALL VALUES IN RADIANS

pi constant 3.14_
radians(x) converts degrees to rad
degrees(x) converts radians to degrees
'''

'''
RANDOM MODULE NOTES

random returns pseudorandom values, they appear random but are
but they are deterministic and predictable. 
This works by using a SEED as an input that is run through an
algorithm that returns a NEW SEED VALUE as an output.


'''