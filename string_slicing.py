# strings slicing study guide

# string slice method: anyString[startInclusive:stopExclusive:Step]
# slice strings by INDEX, last chr in string is HIGHEST INDEX OR -1
# IF COUNTING POSITIVE START WITH 0
# IF COUNTING NEGATIVE START WITh -1
# START INDEX is ALWAYS INCLUDED
#STOP INDEX ALWAYS EXCLUDED

seq: str = '012345'

print(seq[1:3])
print('12')
print()

print(seq[3:])
print('345')
print()

print(seq[:3])
print('012')

print()
print('IF TERMINATES ON NEGATIVE INDEX CONVERT TERMINATOR TO POSITIVE EQUIVALENT, PROCEED.')
print(seq[3:-2])
print('3')

print()
print(seq[-3: 4])
print('3')

print()
print(seq[: : 2])
print('024')

print()
print(seq[1::2])
print('135')

exp: str = 'dogs'

print(exp[1:-1])
print(exp[::2])
print(exp[0:1])
print(exp[-3:-1])
