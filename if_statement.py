# if statement: block of code which will execute if condition is true

age=int(input("How old are you? "))

if age==100:
    print("you were born in old stone age period")
elif age>=18:
    print("You are an Adult")
elif age<=0:
    print("You are an not yet born")
else:
    print("You are a child")