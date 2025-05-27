# function: block of code which is only executed when called upon

def hello():
    print("hello")
    print("Have  a blessed day")
hello()

print("\n")
def hello(name):
    print("Greetings "+name)

hello("Allan")

print("\n")
def area(pi,r):
    area1=pow(pi*r,2)
    print(area1)
area(3.142,2)

print("\n")

def greetings(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name+" you are "+str(age)+" years old")
greetings("Allan","Otieno",24)