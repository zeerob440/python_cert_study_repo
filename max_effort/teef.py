
'''
try = try to do the thing, if not
except = do the thing that failed 
else = do the thing ONLY if except fails
finally always do the thing 


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

    ALWAYS WRITE EXCEPTIONS AS MOST SPECIFIC TO MOST GENERAL; CHILD, THEN PARENT. 

BaseException  = The entire deck
│
├── Exception          = Spades
│     ├── TypeError         = 10♠
│     ├── ValueError        = J♠
│     ├── LookupError       = Q♠
│     │      ├── IndexError = K♠
│     │      └── KeyError   = A♠
│     └── ArithmeticError
│            ├── ZeroDivisionError
│            └── OverflowError
│
├── KeyboardInterrupt = Clubs
├── SystemExit        = Hearts
└── GeneratorExit     = Diamonds

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