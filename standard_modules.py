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

pi #constant 3.14_
e #constant Euler's Number 2.71
radians(x) converts degrees to rad
degrees(x) converts radians to degrees
'''

'''
RANDOM MODULE NOTES

random returns pseudorandom values, they appear random but are
but they are deterministic and predictable. 
This works by using a SEED as an input that is run through an
algorithm that returns a NEW SEED VALUE as an output.

random entities

random()- produces a float between 0 an 1 EXCLUSIVE
seed(intValueGoesHere)- this sets the seed with a desired value
seed() - sets seed with current time 
# IF seed is set, the return values will always be the same with each program run.

INTEGER ENTITIES
THESE Entities return WHOLE NUMBERS
# randrange is RIGHT SIDE EXCLUSIVE ALWAYS
randrange(endIntExclusiveHere)
randrange(startInclusiveHere, endExclusiveHere)
randrange(startInclusiveHere, endExclusiveHere, stepValueHere)

RANDINT
randint is both side inclusive, and return a random whole number
randint()

CHOICE and SAMPLE Functions
choice(enterIterableHere)
returns a prandom item

SAMPLE()
sample(iterableHere, intOfItemsWantedForRandomReturn)


'''
print('seed(0) in action below.\n')
chaos.seed(0)
print("setting the seed to any number always returns the same number.")
print(chaos.random())
print()
print('randrange(), randint() and random() in action\n')

ranint: int = chaos.randint(1, 5)
rando_range: int = chaos.randrange(0, 3)
rando_float: float =chaos.random()
print('Below is randint output it is BOTH SIDE INCLUSIVE')
print(ranint)
print()
print('below is randrange() output, it is RIGHT EXCLUSIVE')
print(rando_range)
print()
print('random() in action below.TAKES NO ARGS returns a float between 0 and 0.99_ \n')
print(rando_float)
print()
print('choice() and sample in action\n')

people: list = ['wafa', 'elaine', 'kristen', 'stefanie', 'nunu']
print('choice returns a single item from an iterable\n')
print(chaos.choice(people))
print()
print('sample() requires 2 args, it returns a specified number of random items from an iterable\n')
print(chaos.sample(people, 2))



