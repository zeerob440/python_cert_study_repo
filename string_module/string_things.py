# this program studies strings

# strings are immutable, this means a string cannot be del(), pop(), append(), insert()

#len function

word: str = 'wow'

print(len(word))
# returns the number of chars in string

# escape character lik \ are not counted
im: str = 'i\'m'
print(len(im))

# len works with multiline strings too
# but each implicit linebreak (\n) adds the n but ignores the \
# so total chars+ number of line breaks = len multiline strings

long_string: str = '''

six'''

print(len(long_string))

# concatenation - adding strings to get her with +
# replicate - 'b' * 4, prints bbbb

# using operators that mean something else outside of strings is called overloading

# replicate string order does not matter

the_devil_u_know: str = 'a' * 4
the_devil_u_dont: str = 4 * 'a'
print(the_devil_u_know, the_devil_u_dont,)

# ord() function
# known as "ordinal"
# returns Unicode code point (number)

t = ord('a')
print(t)

# chr()
# chr uses the code point number to return its associated character
get_char = chr(45)
print(get_char)

# string indexing

index_dis: str = 'dogs'

for rune in index_dis:
    print(rune, end = '')

# append by concatenation
# can add anything on the left or right of initial string, not the middle.

add_to_dis: str = 'hockey puck'
#\n just breaks the previous end = ''
print('\n' + add_to_dis)

# append like concat
add_to_dis: str = 'my ' + add_to_dis
print( add_to_dis)

add_to_dis: str = add_to_dis + ' signed.'

print(add_to_dis)

# min() 
# the min() function returns the min code point value character
print('min(function in action below\n)')
min_max_demo: str = 'aAbw'
print(min(min_max_demo))
print('max() function in action below')
print(max(min_max_demo))

# index() method
# index() returns the first occurrence of a given chr in a string.
print('targetStringHere.index("enterTargetChrHere") method in action below\n')
index_dis: str ='agrltr'
print(index_dis.index('r'))

# list() function, turns a string into a list. 
new_string: str = "AaBb"
print(new_string)
print('list() in action below\n')
new_list: list = (list(new_string))
print(new_list)

# count() method
# count method counts all occurrences of a target string.
print('Count() method in action below.\n')
print(index_dis, '\n')
count_dis = index_dis.count('r')
print(count_dis)