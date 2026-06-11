import module
#prints name of imported module. 
print(module.__name__)
print(__name__)
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))