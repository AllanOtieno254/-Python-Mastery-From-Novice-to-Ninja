text = "This is writing a file\nthis is going to the next line\nwelcome to python"

# Use write mode ('w') to open the file for writing
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\git init.txt", "w") as file:
    file.write(text)


with open("C:\\Users\\Admin\\OneDrive\\Desktop\\git init.txt") as file:
     print(file.read())

print("\n")
# we can use append to prevent when writing the on the file the previous content from dissapearing and being replaced by the current

try:
    import os

    path = "C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt"
    if os.path.exists(path):
        print("file exist")
    else:
        print("path doesnt exist")

    text1 = "Welcome to append\n this is the best method to write a file"
    with open("C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt", "a") as file:
        file.write(text1)

    with open("C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt", "r") as file:
        print(file.read())

except io.UnsupportedOperation as e:
    print(e)
    print("ensure when you want to read the file and you decide to declare reading(r)or writing(w) ensure you do it correctly with whatever action you want to take")
    print("use (r) when reading file and use (w) when writing file")

print("\n")
text2="This is writing a file\nthis is going to the next line\nwelcome to python"
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt", "a") as file:
    file.write(text2)
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt", "r") as file:
        print(file.read())

