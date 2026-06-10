# __preceding a var informs users this is a var and should be unchanged. 
__counter: int = 0
# returns __main_ if run from own program
#print(__name__)

if __name__ == '__main__':
    print('I prefer to be a module.')
else:
    print('I like to be a module.')

def suml(the_list):
    __counter += 1
    the_sum: int = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    __counter += 1
    prod: int = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)

        