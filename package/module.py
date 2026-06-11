# __preceding a var informs users this is a var and should be unchanged. 

# returns __main_ if run from own program
#print(__name__)

#!/usr/bin/env python3 

# module.py - an example of a Python module 

__counter = 0

print(__name__)
def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum


def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod

# __name__ == "__main__" will run a program if it is the own program. 
if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)
  


        