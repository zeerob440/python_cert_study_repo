
d = {"A": 1, "B": 2}

print(d.get("C")) # get returns none. 

try:
    print(d['C']) # returns KeyError
except KeyError: print('d["C"] produces KeyError')

# default value of .get() method
d = {"A": 1, "B": 2}

print(d.get("A", 99)) # since key exists, but value is incorrect, .get() returns 1
print(d.get("C", 99)) # key does not exist, so .get() method returns none.