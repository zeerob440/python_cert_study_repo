from math import factorial

# try-except-else-finally blocks

'''
if the except block does not execute, the the else block executes.

else in this context mean the exception did not happen. 
'''

try:
    print("A")
except Exception:
    print("B")
else:
    print("C")
finally:
    print("D\n")

# .remove() method
'''
.remove method  removes the first occurrence of a value and returns 'None'
'''
x = [1, 2, 3]

print(x.remove(2))
print(x)

f = [3, 4, 5]

try:
    print(f.pop([2]))
except TypeError: print('.pop() targets indexes, but without [] .')
print(f.pop(2))
print(f)

## round() function quirks at .5 it always rounds to the nearest even integer
print(round(2.5), round(3.5), round(3.2))

print('FACTORIAL\n')
# factorial 
# takes the original number, and multiplies it, for the number and every number between it to 1
factorial(0)   # 1
factorial(1)   # 1
factorial(2)   # 2
factorial(3)   # 6
factorial(4)   # 24


print(factorial(5))   # 120

print(5 * 4 * 3 * 2 * 1)