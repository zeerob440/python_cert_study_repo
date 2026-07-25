# try except blocks allow the program to continue even if an error is raised.

'''
Exceptions have hierarchy
1.BaseException contains
    all exceptions
    is the exception used when only
    except:
2. arithmeticError contains
    zeroDivisionError
    overFlowError
3. LookupError contains
    IndexError
    KeyError
4. ImportError contains
    ModuleNotFoundError
5. OSERROR
    FileNotFoundError
6. NameError
    var called with no name
7. TypeError
    when trying to do an op with incompatible data types
8. ValueError
    returns when say a string '3.3' is converted to int

'''
def f(x):
    try:
        x == 1
    except:
        print("a",end='')
    else:
        print("b",end='')
    finally:
        print("c",end='')


f(1)
f(0)

# type testing
fl = 3.3
fl = int(fl)
print(fl)
