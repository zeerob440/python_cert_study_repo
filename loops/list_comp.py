'''
A list comprehension generates a new list from another iterable. Their syntax is similar to how
Yoda speaks, begin reading from the 'for' statement

NOTE: comps cannot use while loops. 

generated list = [varYouWant for elementInExistingIterable in existingIterable]

or 

new_list = [expression for item in iterable]

or

[what_to_store for item in iterable if condition]

think:
what you want
for variable
in collection

or 

[new_item for item in collection]
'''
# existing list
nums = [10, 10, 10]
# new list built with list comprehension
zeroes =[num - 10 for num in nums]
print (zeroes)
print()

cats = ['moose', 'kook', 'Cline']
appended_cats = ['old ' + cat for cat in cats]

print (appended_cats)

numbers = [2, 4, 6, 8 , 10]

# conditionals come after the COMPLETE FOR IN STATEMENT
six_eight_ten_doubled = [num * 2 for num in numbers if num > 5]

print(six_eight_ten_doubled)

# hmmm don't know how to describe this structure, the iterator is at the end in this case
else_list = [num - 2 if num < 5 else num * 2 for num in numbers]

print(else_list)

b
