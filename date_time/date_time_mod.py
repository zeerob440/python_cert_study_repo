import datetime

import time

# get date with .today() method
print(datetime.date.today())

# day, month, and year ar child attributes of .today() method?
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)

# time stamps
# .time() for the time module returns the number of seconds since 1 JAN 1970
time_stamp = time.time()

print(time_stamp)

import datetime

iso_date = datetime.date.fromisoformat("2026-07-02")
print(iso_date)