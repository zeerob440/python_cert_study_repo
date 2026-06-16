# in and not in operators
# in and not in operators return a Bool if a string contains or does not contain something. 

string_theory: str = '5746749808'

print('1' not in string_theory)

print('6' in string_theory)

if '1' in string_theory:
    print('1 is in here.')
else:
    print('Not the 1 you\'re looking for.')