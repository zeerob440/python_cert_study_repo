# this program is for reinforcing import syntax
from package import module
from math import pi as PIE

obj = module.Entity()

obj

'''
or

from package.module import Entity

obj = Entity()

obj
'''
'''
# when alias is used, orginal name no longer accessible
print(PIE)
print(pi) # no longer accessible because of alias, 

'''