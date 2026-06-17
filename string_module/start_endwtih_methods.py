# startswith() and endswith() methods return True/False if a target string starts with or ends with something.
# syntax
# targetString.startswith('targetSequence')
# targetString.endswith('targetSequence')

end_str: str = 'AB CD AB CD'

print(end_str.endswith('D'))
print(end_str.endswith('A'))
print(end_str.startswith('A'))
print(end_str.startswith('D'))