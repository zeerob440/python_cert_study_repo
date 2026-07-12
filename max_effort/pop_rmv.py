
my_compendium = [1, 3, 4, 5, 6, 10]

# .pop() removes the last index and returns the element. .pop(4) removes the element at the 4th index. .pop() DOES NOT TAKE VALUES

print(my_compendium.pop(4))
print(my_compendium) 

# .remove() targets values only AND MUST HAVE AN ARG, returns 'None'

print(my_compendium.remove(10))

print(my_compendium)