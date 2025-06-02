# index_operator[] :gives access to sequences element(str,list,tuples)
from string_slicing import last_name

name="allan Otieno"

print("\n")
if name[0:5].islower():
    print("lowercase")
else:
    print("not lower")

print("\n")
print(name[0:5].upper())

print("\n")
first_name=name[:5]
last_name=name[6:]
print(first_name)
print(last_name)

print("\n")
print(first_name.upper())
print(last_name[-6:].lower())