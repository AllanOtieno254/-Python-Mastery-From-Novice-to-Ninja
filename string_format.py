# str.format: optional method that gives users
#             more control when displaying output

animal="cow"
item="moon"

# print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format("cow","moon"))
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format("cow","moon"))#positional arguments
print("The {animal} jumped over the {item}".format(animal="dog",item="table"))#keyword arguments

name="Allan Otieno"
print("Hello,my name is {}".format(name))

#displaying only the 1st 2 digits of pi
pi=3.14159
number=3.14159
number1=1000
print("The number pi is {:.2f}".format(pi))
print("The number is {:.3f}".format(number))
print("The number {:,}".format(number1))
print("the number {:b}".format(number1))
print("The number {:x}".format(number1))