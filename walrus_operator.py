# walrus_operator:=
#
# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression


# Happy=True
# print(Happy)

print(Happy := True)

# foods=[] #or you can use food=list() since tuple doesnt accept append
# print("when done picking type quite")
# while True:
#     Food_input=input("What food do you like? ")
#     if Food_input=="quit":
#         break
#     foods.append(Food_input)
#     print(foods)
# print(foods)

foods=list()
while food := input("What food do you like? ") !="quit":
    foods.append(food)
