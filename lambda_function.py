# lambda_function:function written in one line using lmbda keyboard
#                 accepts any number of arguments,but only has one expression.
#                 (think of it as a shortcut)
#                 (useful if neede for a short period of time,throw away)
from return_statement import multiply

# syntax:
#func_nam = lambda  parameters:expression

# def double(x):
#     return x*2
# print(double(5))

double=lambda x:x * 2
print(double(2))

multiply = lambda x,y:x*y
print(multiply(3,2))

add= lambda x,y,z: x+y+z
print(add(7,2,3))

full_name= lambda f_name,l_name:f_name+" "+l_name
print(full_name("Allan","Otieno"))

age_check = lambda age: "adult" if age >= 18 else "child"
print(age_check(44))   # Output: adult

# def age_checker1(age=None):
#     try:
#         if age <= 0:
#             print("Invalid age. You are not yet born")
#         elif age >= 18:
#             print("You are an adult")
#         else:
#             print("You are a child")
#     except TypeError as e:
#         print(e)
#         print("Something went wrong. Please insert a value in the function call")
#
# age_checker1(0)  # now works and shows error message


