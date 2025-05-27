#pseudo random number
import random
x=random.randint(1,6)#gives random values between 0 and 6
y=random.random()#gives random values between 0 and 1
print(y)
print(x)

print("\n")
#generating random choice
import random
my_list = ["rock", "paper", "scissors"]
z=random.choice(my_list)
print(z)

print("\n")
import random
my_list = ["rock", "paper", "scissors"]
for _ in range(3):
    choice = random.choice(my_list)
    print(choice)


print("\n")
import random
my_list = ["rock", "paper", "scissors"]
for i in my_list:
    z=random.choice(my_list)
    print(z)

print("\n")
#we can use shufflle to shuffle values eg cards
cards=[1,2,3,4,5,6,7,8,9,"j","Q","K","Ä"]
random.shuffle(cards)
print(cards)

