
try:
    with open("C:\\Users\\Admin\\OneDrive\\Desktop\\git init.txt") as file:  # if file is within the project folder you can just use file name(git init.txt) instead of path
        print(file.read())

except FileNotFoundError as e:
    print(e)
    print("file not found")
    print("check file path")
    print("check on the file format extension")

