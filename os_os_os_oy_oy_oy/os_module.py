import os

'''moving and creating'''

# returns current working directory.
# print(os.getcwd())

# add directory
# places directory in cwd
#os.mkdir('first_dir')
# remove dir
#os.rmdir('first_dir')

# mkdir can be targeted by inserting path as string
# os.mkdir('os_os_os_oy_oy_oy/scd_dir')
def current_working():
    return os.getcwd()

print(current_working())
os.chdir('os_os_os_oy_oy_oy/scd_dir')

print(current_working())
# makedirs makes a directory inside of your CWD
#os.makedirs('thr_dir')

print(current_working())

#print (os.listdir())
# removes directories
#os.rmdir('thr_dir')

print(current_working())
os.chdir('../../')

print(current_working())
#os.makedirs('date_time')





