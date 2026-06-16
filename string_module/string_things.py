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

