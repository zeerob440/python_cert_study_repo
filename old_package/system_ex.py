import sys

'''
In Python there is a list that stores all locations and directories related to an application 
 path() entity in the system module prints:
    the first path the command was invoked from
    since it is iterating through a list, it iis best to use a for loop. 

'''
for path in sys.path:
    print(path)
# how to add a folder to a file path
#sys.path.append()
