

import os

source = "C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt" #if the file is just located here in this directory you can just type file name eg example.txt otherwise use file path

destination = "C:\\Users\\Admin\\OneDrive\\Documents\\write.txt"

try:
    if os.path.exists(destination):
        print("There's already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")

except FileNotFoundError:
    print(source + " was not found")
