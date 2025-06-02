# loop: statement that will execute block of code limited amount of time
# difference: while loop=unlimite
#             for loop=limited

for i in range(10):
    # print(i+1)
    # i+=2
    # print(i)
    print(i)

for i in "Allan Otieno":
    print(i)

# inlusive and exclusive numbers in for loops

for i in range(50,100): #50 is inclusive and 100 exclusive values. so well print values as from 50 to 100
    print(i)

array = (11, 32,13, 34, 55, 66, 77, 82, 29)
for i in array:
    print(i)
    print(array[4])

# PROJECT
import time
for seconds in range(10, 0, -1):  # start=10, stop=0 (exclusive), step=-1
    print(seconds)
    time.sleep(2)
print("Happy New Year!")

