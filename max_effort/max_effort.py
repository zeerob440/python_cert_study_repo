
# is gotcha

a: int = 5
b: int = 5

print(a is b)
print( a == b)

'''
because == means same value
is means same object-instance
it considers a and b as the same object-instance because of INTERNMENT/CACHING. 
Python will reuse objects if they are INTEGERS between -5 - 256.

'''
print('join() gotchas\n')
try:
    d = {
    "A": 1,
    "B": 2,
    "C": 3
    }

    print("".join(d.values()))
except TypeError:(print(".join() only works on strings.\n"))

# interestingly, .join method can be used to split a sting with a delimiter, but it returns STRING
s = "Python"

print(",".join(s))
print()

print('shallow copies\n')

x = [1, 2, 3]
y = x[:]# this split, only appends the y object and not the x object
# it essentially splits the list object into two lists. 

y.append(4)

print(x) 
print(y)
print()

print('Weird list multiplication property.\n')
# if a list is multiplied, it repeats the list inside the same list.

x = [1, 2, 3]

print(x * 2 + '\n')




