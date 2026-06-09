import math, random
# imports can be imported on the same line if delimited with a comma.
# imports can be declared anywhere in a program, but are typically declared on the top line. 

# OR specific entities can be imported by from moduleName import entityName
from statistics import mean

# multiple entities can be imported from one module such that:
from datetime import date, datetime

''' to call an ENTITY inside a module write:

 moduleNameHere.entityNameHere  
EXAMPLE: math.sqrt
 '''

mathy_thing: float = math.sqrt(25)
print(mathy_thing)

'''specific entity 'mean' imported from module 'statistics
When only an entity is imported from a module, only the entity name is needed to call the entity.

from statistics import mean

mean(enterStructureToApplyEntityTo)

this is known as "accessible without qualification"''' 

numbers: list = [1, 100]

average: float = mean(numbers)

print(average)

# imported entities from datetime

print (date.today())
print (datetime.now())