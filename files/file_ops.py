'''
The basic jist of file is: they need to be open(), read/write, append then close()

ALWAYS:

with open('path/file.txt', 'r') as varName

with always ensures the file is close() after operation is complete
'''
# how to open an read a file with .read() method. 'r' == 'rt'
with open('files/git_bash_documentation.txt', 'r') as file:
    pass
    # print(file.read())

# how to write to a file with .write() method
# 'w' == 'wt' overwrites the entire file .write() also ovewrites an entire file
with open('files/crud.txt', 'w') as file2:
    file2.write('This is how to write to a file')

with open('files/crud.txt', 'r') as file2:
    print(file2.read())
print()

print("'a' in use\n")
# how to append a file with .write() method
# use 'a' to append in var declaration, adds to does not delete file data like 'w'
with open('files/crud.txt', 'a') as file2:
    file2.write('\nThis is the appended line.')

with open('files/crud.txt', 'r') as file2:
    print(file2.read())

# how to read a single line with readline()
# readline() returns a string.
print()
with open('files/crud.txt', 'r') as file2:
    # will print first line of file
    print('this is readline() in use. It only reads oneline per call in the with open block.\n')
    print(file2.readline())

print()

# readlines() method appends lines into a list
# readlines() can take an int arg, the int is the number of bytes you want it to read. 

with open('files/crud.txt', 'r') as file2:
    # save files into a list
    lines: list = file2.readlines()
    # read list
    print(list(lines))

print()
# how to read and write in the same with open() block operation with 'r+'
# .seek() method needs to be used with this. .seek() controls the cursor.
# to first you need to move the cursor to EOF == seek(0, 2) tow write the file wo overwriting 
# then to read the file, the cursor must be moved to SOF == seek(0)
# .tell() tells you were the cursor is in a file. 
print("r+ demo\n")

with open('files/crud.txt', 'r+') as file2:
    # move cursor to end of file
    print(f'Cursor is here in bytes: {file2.tell()}')
    file2.seek(0, 2)
    print(f'Cursor is here in bytes: {file2.tell()}')
    file2.write('\nThis was added with "r+".')
    # move cursor back to start of file
    file2.seek(0)
    print(f'Cursor is here in bytes: {file2.tell()}')
    print(file2.read())

# write and update 'w+'
