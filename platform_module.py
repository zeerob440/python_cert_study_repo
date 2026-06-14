import platform
# platform allows you to access your machine's hardware, OS, and terp
'''
Python programs work like this:
1. The developer writes the program and runs it
2. Python accepts the commands from the program, reconstitutes it to meet the OS expectations.
3. OS verifies the request is logical, and attempts to create a file
4. Hardware is activated by the OS commands using Python's written instructions.

PLATFORM ENTITIES 
platform() does not return particularly useful info.
machine() returns processor architecture info
processor() returns processor info suc as type, step, etc. 
system() returns os name such as "windows" or "mac"
version() returns system version numbers.
python_implementation() returns string denoting your python implementation
python_version_tuple() returns the major python version, minor part and patch number
'''

print(dir(platform))

# platform function (entity)

print('platform.platform() in action below')
dis_platform = platform.platform()
print()
print(dis_platform)
print()
print('machine() returns processor architecture it is  in action below\n')
print()
dis_machine = platform.machine()
print(dis_machine)
print('processor() returns info about machines processor below\n')
dis_cpu = platform.processor()
print(dis_cpu)
print()
print('system() returns operating system name such as "windows" or "mac"\n')

dis_system = platform.system()
print(dis_system)
print()

print('version() returns version info such as a release number. in action below\n')
dis_sys_version = platform.version()
print(dis_sys_version)
print()

print('python_implementation in action, platform.python_implementation \n')
print(platform.python_implementation())
print()

print('python_version_tuple() in action below ONLY PRINT IN FOR LOOP\n')
for items in platform.python_version_tuple():
    print(items)
print()