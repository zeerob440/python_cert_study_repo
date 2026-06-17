# startswith() and endswith() methods return a bool if a target string starts with or ends with something

end_str: str = 'AB CD AB CD'

print(end_str.endswith('D'))
print(end_str.endswith('A'))
print(end_str.startswith('A'))
print(end_str.startswith('D'))