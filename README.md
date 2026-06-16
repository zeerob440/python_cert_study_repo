# PCAP Certified Associate Python Programmer study repo

This repo is for archiving, versioning, and studying for the PCAP Certification.

## Module One Notes

- Code tends to grow over time.
- Given scale of a project code should be broken up into several files 

 - decomposition - dividing a large program into several smaller ones.
 - Python Standard Library - Python's official standard library containing all of Python's standard modules.

 - namspace - A namespace is a mapping between names and objects that allows Python to organize variables, functions, classes, and modules while avoiding naming
 conflicts.
    * inside namespaces, each name must be unique. However names can be the same inside of different modules.

### Working with Standard Modules

dir(moduleNameOrAliasName)- returns an alphabetical list of all entities in a module.

the dir() command can be used directly in a console after the module has been imported.
- just because a package is imported, does not mean entities in the package are implicitly reachable. 
- when you run a file directly, its __name__ variable is set to __main__;
- when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)

### Packages

- practically a package is a folder with an __init__.py declared in it. 

- Package is a container for modules
- Module is a container for functions

so the hierarchy goes: Package, module, function.

in other words a package is a folder full of modules.

- separation of concerns applies to packages.

When packages are created and modules are imported a __pycache__ file appears in the package container.
This __pycache__ contains .pyc files not readable by humans and contains semi-compiled python code ready for Pythons terp.
- this is why imports happen faster, each time after the initial import. 

- when modules are imported, they are implicitly executed by Python, therefore initialization only has to occur once per program.
- when running a program from it's own program __name__ will return __main__
- if the program is imported to another program the name becomes nameOfProgram sans .py. 

### PIP

PyPI (Python Package Index) is the Python central repository maintained by the PYTHON SOFTWARE FOUNDATION
- PyPY repo is know as the 'Cheese Shop" named after a Monty Python skit. 
- PyPI is free of charge.
- pip the installer for PyPI or the Cheese Shop

### useful Pip commands
1. pip show moduleName
returns:
* name
* version
* summary
* Requires
- what other modules this package needs to work
* Required-by
- Which installed packages are required by this package. 

2. pip list
* show all locally installed python modules

3. pip uninstall moduleName
* uninstalls targeted module

4. pip install moduleName
* installs targeted module

## Module 2 notes

### characters

ASCII - American Standard Code for Information Interchange
* uses 256 characters

I18N- Internationalization
* use 18 different letters

code point - a number that is used to make a character

Unicode- uses unique characters to more than 1milli code points. stores files in computer memory such as 
* UCS-4 (universal character set) uses 4 bytes to store each char
* BOM (byte order mark)-unprintable combination of bits announcing if the file is UCS-4 or UTF-8
* UTF-8 (uniform Transformation Format) - uses as many bits as for code points. 8 bits for ASCII, 16 bits for non-latin and 24 bits for CJK (china, japan, korea)

### attributes of strings

String are:
* immutable

len()
* does not count escape characters
* if string is empty, it will return 'empty' 

overloading- using operators that do one thing outside a string, but do another thing inside the string.

