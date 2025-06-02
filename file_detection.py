import os

#checking to see if file exists in our computer
path="C:\\Users\\Admin\\OneDrive\\Desktop\\allano.txt" #if you paste the location:C:\Users\Admin\OneDrive\Desktop just add for each backslash add one more and at the end of
                                                        #file path add the name of the file(eg allano.txt) since in the location was not included
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path): #incase you are using a folder instead of file
        print("That is a directory/folder")
else:
    print("location doesnt exist")