# tuple: collection which is ordered and unchangeable
#         used to group together related data

student=("Allan",24,"male")

#functions related to tuples
print(student.count("Allan"))
print(student.index("male"))

for x in student:
    print(x)

students = ["John", "Mary", "Allan", "Steve"]  # example list

if "Allan" in students:
    print("Hello Allan")
else:
    print("student doesn't exist")

