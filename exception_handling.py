# exception:events detected during execution that interrupt the flow of a program
from logging import exception

try:
    numerator=int(input("Enter your numerator "))
    denominator=int(input("Enter your denominator "))
    result=numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero")

except ValueError as e:
    print(e)
    print("Enter only numbers please")

# # except Exception as e:
#       print(e)
# #     print("Something went wrong")

else:
    print(result)


finally:
    print("This will always execute")


print("\n")

try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")
except ValueError as e:
    print(e)
    print("only enter numerical/number values")


