import hashlib

import random as chaos
'''
dir()
dir() returns a list of entities within a module as seen below

'''
print('dir() is action below\n')
contents = dir(hashlib)

print(contents)
print('alias dir() example below\n')
# If a module has been imported with an alias dir(alias)
contents_content = dir(chaos)

print (chaos)