# this program studies strings

# strings are immutable 

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
print(the_devil_u_know, the_devil_u_dont, end = ',')