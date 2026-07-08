
d = {"A": 1, "B": 2}

print(d.get("C")) # get returns none. 

try:
    print(d['C']) # returns KeyError
except KeyError: print('d["C"] produces KeyError')
