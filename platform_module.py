import platform
# platform allows you to access your machine's hardware, OS, and terp
'''
Python programs work like this:
1. The developer writes the program and runs it
2. Python accepts the commands from the program, reconstitutes it to meet the OS expectations.
3. OS verifies the request is logical, and attempts to create a file
4. Hardware is activated by the OS commands using Python's written instructions.
'''

print(dir(platform))

# platform function (entity)

dis_machine = platform.platform()
print(dis_machine)