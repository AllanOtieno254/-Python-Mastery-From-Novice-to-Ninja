# exception:events detected during execution that interrupt the flow of a program
from logging import exception

try:
    numerator=int(input("Enter your numerator "))
    denominator=int(input("Enter your denominator "))
    result=numerator / denominator
    print(result)
except Exception:
    print("Something went wrong")