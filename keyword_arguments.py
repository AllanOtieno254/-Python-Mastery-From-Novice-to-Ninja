# keyword_arguments: arguments preceeded by an identifier when we pass them to a function
#                     The order of argument doesnt matter,unlike positional arguments
#                     python knows the names of the arguments that our function receives

#positional arguments
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello("allan","otieno","akumu")
hello("otieno","allan","akumu")

# keyword_arguments:
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(middle="Otieno",last="akumu",first="allan")