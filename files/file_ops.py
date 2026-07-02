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

print("The file with the added line.\n")
# how to append a file with .write() method
# use 'a' to append in var declaration, adds to does not delete file data like 'w'
with open('files/crud.txt', 'a') as file2:
    file2.write('\nThis is the appended line.')

with open('files/crud.txt', 'r') as file2:
    print(file2.read())

# how to read and write in the same operation with 'r+'
print("r+ demo\n")

with open('files/crud.txt', 'r+') as file2:
    file2.write('\nThis was added with "r+".')

    print(file2.read())

# write and update 'w+'
#   