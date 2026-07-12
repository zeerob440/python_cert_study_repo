
'''
try = try to do the thing, if not
except = do the thing that failed 
else = do the thing ONLY if except fails
finally always do the thing 

'''
# just comment out x = 1 to see how program run time changes. 
x = 1 


try:
    x == 1 
except:
    print('x does not equal 1\n')
else:
    print('else in teef blocks, executes if the try block executes and the except block DOES NOT EXECUTE')
    print('x deffo equals 1\n')
finally:
    print('Finally blocks always execute')