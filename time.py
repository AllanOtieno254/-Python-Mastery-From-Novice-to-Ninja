import time

#how to find epoch
#epoch: a date and time from which a computer measures system time

print(time.ctime(1000000)) #converts a time expressed in seconds sets epoch to a readable string
                    #epoch=when your computer thinks time began(reference point)


print(time.time()) # returns current seconds since epoch

time_object=time.localtime()
print(time_object)
local_time=time.strftime("%B,%d,%Y,%H",time_object)
print(local_time)

print("\n")
from datetime import datetime

time_string = "20 April, 2025"
time_object = datetime.strptime(time_string, "%d %B, %Y")  # convert string to datetime object
formatted = time_object.strftime("%d,%B,%Y")               # format datetime object
print(formatted)
