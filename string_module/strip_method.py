# studies lstrip(), rstrip(), and strip()

strip_poker: str = '---10-jqa---'

# .strip() remove all left or right consecutive whitespace if no target specified, or targeted char
print(strip_poker.strip('-'))

# lstrip() does the same as strip, but starts from the left side of the string.
# when the last consecutive target char is removed, it stops.
# rstrip() does the opposite 

print(strip_poker.lstrip('-'))
print(strip_poker.rstrip('-'))