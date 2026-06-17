#rfind() method
# syntax
#targetString.rfind('is',inclusiveStart, exclusiveEnd)
# rfind() searches a string starting from the right, 
# it returns the first indice from the right the object lives or -1 if not found
# NOT VERY USEFUL

tau_str: str = 'abcdefghijk'

print(tau_str.rfind('f'))
# or 
print(tau_str.rfind('b', 0, 5))

print(tau_str.rfind('d', 4, 8))
