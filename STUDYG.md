PCAP Library & Method Study Guide (Explained)

This guide explains what each required PCAP method does, when to use it, and its syntax.

# math

Method                  What it does            Syntax

math.ceil(x)          Rounds a number up math.ceil(3.2)toward positive infinity.

math.floor(x)         Rounds a number down math.floor(3.8)toward negative infinity.

math.trunc(x)         Removes the decimal math.trunc(-3.9)portion (toward zero).

math.factorial(n)     Computes n! (n × n-1  math.factorial(5)× ... × 1).

math.sqrt(x)          Returns the square root math.sqrt(25)as a float.

# random

Method                   What it does            Syntax

random.random()        Returns a random  random.random()floating-point number from 0.0 up to but not including 1.0.

random.seed(n)         Initializes the random  random.seed(10)number generator so the same "random" sequence can be reproduced.

random.choice(seq)     Returns one random      random.choice(colors)element from anon-empty sequence.

# platform

Method                               What it does

platform.platform()                Returns a descriptive string about the operating system.

platform.machine()                 Returns the machine architecture(x86_64, AMD64, arm64, etc.).

platform.processor()               Returns processor information.

platform.system()                  Returns the operating system family(Windows, Linux, Darwin).

platform.version()                 Returns the operating system version string.

platform.python_implementation()   Returns the Python implementation(usually CPython).

# sys

sys.path

sys.path is a list of directories Python searches when you import a module.

Example:

import sys
print(sys.path)
sys.path.append("/my/modules")

# errno

Constant   Meaning

ENOENT   File or directory does not exist.
EACCES   Permission denied.
EEXIST   File already exists.

Import Syntax

import math                  # import entire module
from math import sqrt        # import one object
from math import sqrt, floor # import several objects
import math as m             # alias
from math import *           # import everything (not recommended)

String Methods

Method                              Purpose

.isalpha()                        True if every character is aletter.

.isdigit()                        True if every character is a digit.

.isalnum()                        True if letters and/or digits only.

.isspace()                        True if only whitespace characters.

.islower()                        True if all letters are lowercase.

.isupper()                        True if all letters are uppercase.

.istitle()                        True if every word starts with a capital letter.

.join(iterable)                   Joins strings together using the calling string as the separator.

.split()                          Splits a string into a list.

.strip()                          Removes whitespace (or specified characters) from both ends.

.find()                           Returns the first index of a substring or -1.

.rfind()                          Returns the last index of a substring or -1.

.index()                          Like find(), but raisesValueError if missing.

.upper()                          Returns an uppercase copy.

.lower()                          Returns a lowercase copy.

.capitalize()                     Capitalizes only the first letter.

.title()                          Capitalizes the first letter of every word.

.swapcase()                       Swaps uppercase to lowercase and vice versa.

.replace(old,new)                 Replaces matching text with new text.

.startswith(x)                    Tests whether a string begins with x.

.endswith(x)                      Tests whether a string ends with x.

Remember: Strings are immutable. These methods return new strings.

File Methods

Method                              Purpose

open()                            Opens a file and returns a file object.

.read()                           Reads all (or a specified number of) characters/bytes.

.readline()                       Reads one line.

.readlines()                      Reads every remaining line into a list.

.write()                          Writes text or bytes to a file and returns the number written.

bytearray A bytearray stores mutable binary data. Unlike bytes, individual values can be changed    after creation.

Built-ins

Function                            Purpose

dir(obj)                          Lists an object's available names/attributes.

ord(c)                            Converts one character into itsUnicode integer value.

chr(n)                            Converts a Unicode integer into its character.

sorted(iterable)                  Returns a new sorted list.

hasattr(obj,name)                 Returns True if the object has the named attribute.

isinstance(obj,type)              Returns True if an object belongs to a class (or subclass).

map(func,it)                      Applies a function to every element and returns a map iterator.

# OOP

Name           Purpose

__init__     Constructor used to initialize new objects
.__str__()     Controls what print(obj) displays
.__dict__     Dictionary of an object's stored attributes
.__module__   Module where the class was defined.__name__     Name of a class or module.__bases__    Tuple containing a class's parent class(es).self Reference to the current object
.super()      Calls methods from the parent class.

# Exceptions

try: code that may fail.

except: handles an exception.

else: runs only if no exception occurs.

finally: always runs.

raise: intentionally throws an exception.

.args: tuple containing arguments passed to the exception.

PIP

python -m pip install package --- install a package.

python -m pip uninstall package --- remove a package.

python -m pip list --- list installed packages.

python -m pip show package --- display package information.

python -m pip freeze --- output installed packages for requirements files.