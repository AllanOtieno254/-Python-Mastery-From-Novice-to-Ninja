# zip_function():aggregate elements from two or more iterables(list,tuple,sets etc)
#                 creates a zip object with paired elements stored in tuple for each element

username=["Allan","Duke","Hister"]
password=("pass@234","abc123","guest")

users=zip(username,password)
for i in users:
    print(i)

print("\n")
# changing to dictionary
username = ["Allan", "Duke", "Hister"]
password = ["pass@234", "abc123", "guest"]

users = dict(zip(username, password))

for key, value in users.items():
    print(key, value)


