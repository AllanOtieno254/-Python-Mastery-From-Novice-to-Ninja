# args: parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

#can be used to use as many arguments as you want incae you dont want to list all if there are many

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3))