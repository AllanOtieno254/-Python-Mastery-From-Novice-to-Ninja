# import os
# os.remove("del.txt")

#or
# path=("del.txt")
# os.remove(path)

#attempting to delete file that doesnt exist
import os
import shutil

path = "C:\\Users\\Admin\\OneDrive\\Documents\\write.txt"
path1= "C:\\Users\\Admin\\OneDrive\\Documents\\emptyfolder"
path2="C:\\Users\\Admin\\OneDrive\\Documents\\emptyfolder2"

try:
    os.remove(path) # this function doesnt delete empty folder
    os.rmdir(path1) # deleting empty folder
    os.rmtree(path2) #delete folder wuth files in it

except FileNotFoundError as e:
    print(e)
    print("That file was not found")
except PermissionError:
    print("you cannot delete empty folder")
except OSError:
    print("you cannot delete that using that function")
else:
    print(path1+"was deleted")
