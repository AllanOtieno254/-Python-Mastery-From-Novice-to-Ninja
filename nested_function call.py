# nested function call: function call inside another function calls
#                         innermost functions are resolved first
#                         returned value is used as an argument for the next outer function

# num=input("Enter a whole positive number: ")
# num=float(num)
# num=abs(num)
# num=round(num)
# print(num)

# using now nested function call to perform above
print(round(abs(float(input("Enter a whole positive number: ")))))
