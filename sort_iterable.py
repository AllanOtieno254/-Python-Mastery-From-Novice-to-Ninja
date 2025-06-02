from tuple import student

name = [1, 2, 3, 4, 5]
name.sort(reverse=False)
print(name)# ✅ Prints [1, 2, 3, 4, 5]


name = [1, 2, 3, 4, 5]
name.sort(reverse=True)  # ✅ Sorts in descending order
print(name)              # Output: [5, 4, 3, 2, 1]

name = [1, 2, 3, 4, 5]
print(sorted(name, reverse=True))  # Output: [5, 4, 3, 2, 1]

# sort() method:used with lists
# sort() function:used with iterables

students=["squidward","sandy","patrick","spongebob","mr.crabs"]
students.sort(reverse=True)
# print(students)
for i in students:
    print(i)

print("\n")
#sorted iterable
sorted_iterable=sorted(students)
for i in sorted_iterable:
    print(i)

print("\n")
#using key arguments in sorting
#students will be sorted by grades
grades=lambda grade:grade[1]
students1=[("squidward","F",60),
           ("sandy","A",33),
           ("patrick","D",30),
           ("spongebob","B",20),
           ("mr.crabs","C",78)]

students1.sort(key=grades,reverse=True)
for i in students1:
    print(i)

