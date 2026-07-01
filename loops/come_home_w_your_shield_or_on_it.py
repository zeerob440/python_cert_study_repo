
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