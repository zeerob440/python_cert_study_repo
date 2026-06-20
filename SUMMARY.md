# SECTION SUMMARIES OF CISCO CERT CLASS
## Packages
1. While a module is designed to couple together some related entities such as functions, variables, or constants, a package is a container which enables the coupling of several related modules under one common name. Such a container can be distributed as-is (as a batch of files deployed in a directory sub-tree) or it can be packed inside a zip file.


2. During the very first import of the actual module, Python translates its source code into a semi-compiled format stored inside the pyc files, and deploys these files into the __pycache__ directory located in the module's home directory.


3. If you want to tell your module's user that a particular entity should be treated as private (i.e. not to be explicitly used outside the module) you can mark its name with either the _ or __ prefix. Don't forget that this is only a recommendation, not an order.


4. The names shabang, shebang, hasbang, poundbang, and hashpling describe the digraph written as #!, used to instruct Unix-like OSs how the Python source file should be launched. This convention has no effect under MS Windows.


5. If you want convince Python that it should take into account a non-standard package's directory, its name needs to be inserted/appended into/to the import directory list stored in the path variable contained in the sys module.


6. A Python file named __init__.py is implicitly run when a package containing it is subject to import, and is used to initialize a package and/or its sub-packages (if any). The file may be empty, but must not be absent.

## Strings
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

1. Strings can be compared to other strings using general comparison operators, but comparing them to numbers gives no reasonable result, because no string can be equal to any number. For example:

string == number is always False;
string != number is always True;
string >= number always raises an exception.
2. Sorting lists of strings can be done by:

a function named sorted(), creating a new, sorted list;
a method named sort(), which sorts the list in situ
3. A number can be converted to a string using the str() function.

4. A string can be converted to a number (although not every string) using either the int() or float() function. The conversion fails if a string doesn't contain a valid number image (an exception is raised then).

1. Strings are key tools in modern data processing, as most useful data are actually strings. For example, using a web search engine (which seems quite trivial these days) utilizes extremely complex string processing, involving unimaginable amounts of data.

2. Comparing strings in a strict way (as Python does) can be very unsatisfactory when it comes to advanced searches (e.g. during extensive database queries). Responding to this demand, a number of fuzzy string comparison algorithms has been created and implemented. These algorithms are able to find strings which aren't equal in the Python sense, but are similar.

One such concept is the Hamming distance, which is used to determine the similarity of two strings. If this problem interests you, you can find out more about it here: https://en.wikipedia.org/wiki/Hamming_distance. Another solution of the same kind, but based on a different assumption, is the Levenshtein distance described here: https://en.wikipedia.org/wiki/Levenshtein_distance.

3. Another way of comparing strings is finding their acoustic similarity, which means a process leading to determine if two strings sound similar (like "raise" and "race"). Such a similarity has to be established for every language (or even dialect) separately.

An algorithm used to perform such a comparison for the English language is called Soundex and was invented – you won't believe – in 1918. You can find out more about it here: https://en.wikipedia.org/wiki/Soundex.


4. Due to limited native float and integer data precision, it's sometimes reasonable to store and process huge numeric values as strings. This is the technique Python uses when you force it to operate on an integer number consisting of a very large number of digits.

### try except

Don't forget that:

* the except branches are searched in the same order in which they appear in the code;
* you must not use more than one except branch with a certain exception name;
* the number of different except branches is arbitrary – the only condition is that if you use try, you must put at least one except (named or not) after it;
* the except keyword must not be used without a preceding try;
* if any of the except branches is executed, no other branches will be visited;
* if none of the specified except branches matches the raised exception, the exception remains unhandled (we'll discuss it soon)
* if an unnamed except branch exists (one without an exception name), it has to be specified as the last.

1. You cannot add more than one anonymous (unnamed) except branch after the named ones.
2. All the predefined Python exceptions form a hierarchy, i.e. some of them are more general (the one named BaseException is the most general one) while others are more or less concrete (e.g. IndexError is more concrete than LookupError).

You shouldn't put more concrete exceptions before the more general ones inside the same except branche sequence. For example, you can do this:

3. The Python statement raise ExceptionName can raise an exception on demand. The same statement, but lacking ExceptionName, can be used inside the except branch only, and raises the same exception which is currently being handled.


4. The Python statement assert expression evaluates the expression and raises the AssertError exception when the expression is equal to zero, an empty string, or None. You can use it to protect some critical parts of your code from devastating data.
### oop
1. A class is an idea (more or less abstract) which can be used to create a number of incarnations – such an incarnation is called an object.


2. When a class is derived from another class, their relation is named inheritance. The class which derives from the other class is named a subclass. The second side of this relation is named superclass. A way to present such a relation is an inheritance diagram, where:

superclasses are always presented above their subclasses;
relations between classes are shown as arrows directed from the subclass toward its superclass

3. Objects are equipped with:

a name which identifies them and allows us to distinguish between them;
a set of properties (the set can be empty)
a set of methods (can be empty, too)

4. To define a Python class, you need to use the class keyword. 

5. To create an object of the previously defined class, you need to use the class as if it were a function. For example instance_name = ClassName()

1. A stack is an object designed to store data using the LIFO model. The stack usually performs at least two operations, named push() and pop().


2. Implementing the stack in a procedural model raises several problems which can be solved by the techniques offered by OOP (Object Oriented Programming).


3. A class method is actually a function declared inside the class and able to access all the class's components.


4. The part of the Python class responsible for creating new objects is called the constructor, and it's implemented as a method of the name __init__.


5. Each class method declaration must contain at least one parameter (always the first one) usually referred to as self, and is used by the objects to identify themselves.


6. If we want to hide any of a class's components from the outside world, we should start its name with __. Such components are called private.