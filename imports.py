import math, random
# imports can be imported on the same line if delimited with a comma.
# imports can be declared anywhere in a program, but are typically declared on the top line. 
# OR specific entities can be imported by  
from statistics import mean

''' to call an ENTITY inside a module write:

 moduleNameHere.entityNameHere  
EXAMPLE: math.sqrt
 '''

mathy_thing: float = math.sqrt(25)
print(mathy_thing)

# specific entity 'mean' imported from module 'statistics' 

numbers: list = [1, 100]

average: float = statistics.mean(numbers)