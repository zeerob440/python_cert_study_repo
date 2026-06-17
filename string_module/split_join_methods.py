# split() method
# builds a list from a string and a delimiter, whitespace is default delimiter
# very useful

str9: str = 'a;b c;d e;f g;h i;j k;'

print(str9.split())
# note if delimiter is last value, an empty list element will be created
print(str9.split(';'))
print()

# join() joins iterables containing all strings together as strings, has strange syntax
# syntax
# 'joinDelimit'.join(targetIterableContainingOnlyStrings)

join_list: list = ['1a', '2b', '3c']
join_dict: dict = {'dog': 'rico', 'cat': 'moose'}
join_tup: tuple = ('sgt johnson', 'MA5B')

print('-'.join(join_list))
print('^'.join(join_dict))
print('#'.join(join_tup))

