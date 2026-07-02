
# lambda functions
# structure
# name = lambda parameters: return_value

# traditional function
def shout(name):
    return name.upper()

print(shout("rico"))

# equal lambda function, args, if any go next to lambda followed by a : it can take 0 - inf args
shout = lambda name: name.upper()

print(shout("rico"))

double = lambda x: x * 2

print(double(2))

triple_10 = lambda x2, x10: (x2 * 3, x10 * 10)

print(triple_10(3, 5))

# map()
#map(function, iterable)
# takes a function and adds the result to an iterable
# map creates generator object, it must be extracted with an iterable. 
dogs =['mia', 'rico', 'orion']

result = map(lambda dog: dog.upper(), dogs)
# object extracted as list. 
print (list((result)))

# be sure to pass minimum needed args in the function
def addGoodBoy(dog):
    return f'{dog} Is good boy!'
# converts map generator object to list
gb_result = list(map(addGoodBoy, dogs))

print(gb_result)

# filter()
# filter(function, iterable)
# creates a generator-object that must be extracted with an iterable

def dogFilter(dog):
        return len(dog) == 4

fun_result = list(filter(dogFilter, dogs))
print(fun_result)

f_result = list(filter(lambda dog: len(dog) == 4, dogs))

print(f_result)



