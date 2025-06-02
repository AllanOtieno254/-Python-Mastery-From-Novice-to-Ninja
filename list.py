# list:used to store multiple items in a single variable
food = ["piza","chicken","hotdog","spaghetti"]
print(food)
print(food[1])

food[0]="sushi"
print(food[0])
print(food)

for i in food:
    print(i)

print("\n")

#LIST FUNCTIONS
food.append("icecream") #adds an element at the end of list

food.remove("hotdog") #removes specific element

food.pop() #removes the last element

food.insert(0,"cake")

food.sort()

for i in food:
    print(i)