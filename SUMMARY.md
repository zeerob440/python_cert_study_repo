# SECTION SUMMARIES OF CISCO CERT CLASS
## Packages
1. While a module is designed to couple together some related entities such as functions, variables, or constants, a package is a container which enables the coupling of several related modules under one common name. Such a container can be distributed as-is (as a batch of files deployed in a directory sub-tree) or it can be packed inside a zip file.


2. During the very first import of the actual module, Python translates its source code into a semi-compiled format stored inside the pyc files, and deploys these files into the __pycache__ directory located in the module's home directory.


3. If you want to tell your module's user that a particular entity should be treated as private (i.e. not to be explicitly used outside the module) you can mark its name with either the _ or __ prefix. Don't forget that this is only a recommendation, not an order.


4. The names shabang, shebang, hasbang, poundbang, and hashpling describe the digraph written as #!, used to instruct Unix-like OSs how the Python source file should be launched. This convention has no effect under MS Windows.


5. If you want convince Python that it should take into account a non-standard package's directory, its name needs to be inserted/appended into/to the import directory list stored in the path variable contained in the sys module.


6. A Python file named __init__.py is implicitly run when a package containing it is subject to import, and is used to initialize a package and/or its sub-packages (if any). The file may be empty, but must not be absent.

1. Computers store characters as numbers. There is more than one possible way of encoding characters, but only some of them gained worldwide popularity and are commonly used in IT: these are ASCII (used mainly to encode the Latin alphabet and some of its derivates) and UNICODE (able to encode virtually all alphabets being used by humans).

2. A number corresponding to a particular character is called a codepoint.

3. UNICODE uses different ways of encoding when it comes to storing the characters using files or computer memory: two of them are UCS-4 and UTF-8 (the latter is the most common as it wastes less memory space).

1. Python strings are immutable sequences and can be indexed, sliced, and iterated like any other sequence, as well as being subject to the in and not in operators. There are two kinds of strings in Python:

one-line strings, which cannot cross line boundaries – we denote them using either apostrophes ('string') or quotes ("string")
multi-line strings, which occupy more than one line of source code, delimited by trigraphs:


2. The length of a string is determined by the len() function. The escape character (\) is not counted. For example:

3. Strings can be concatenated using the + operator, and replicated using the * operator. For example:

4. The pair of functions chr() and ord() can be used to create a character using its codepoint, and to determine a codepoint corresponding to a character. Both of the following expressions are always true:


5. Some other functions that can be applied to strings are:

list() – creates a list consisting of all the string's characters;
max() – finds the character with the maximal codepoint;
min() – finds the character with the minimal codepoint.

6. The method named index() finds the index of a given substring inside the string.