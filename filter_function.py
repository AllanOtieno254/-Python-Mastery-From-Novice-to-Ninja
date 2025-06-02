# filter(): creates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

friends = [("Allan", 20),
           ("peter", 16),
           ("charity", 19),
           ("Damaris", 17),
           ("kimkim", 15),
           ("sebu", 26)]

# Function to check if age is 18 or older
drinking_friends = lambda person: person[1] >= 18

drinking_buddies = list(filter(drinking_friends, friends))
# print(drinking_buddies)

for i in drinking_buddies:
    print(i)

print("\n")
students=[10,20,30,40,50,0,60,70,80,90,100]
above_grades=list(filter(lambda grades:grades>=60,students))
print(above_grades)
