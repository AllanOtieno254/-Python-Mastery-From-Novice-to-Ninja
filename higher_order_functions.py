# higher_order_functions: a function that either:
#                             1.accept a function as an argument
#                             2.or returns a function
#                             (in python functions are also treated as objects)
#

#1. accepts function as an argument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text=func("Hello world") # it tries to call func
    print(text)
hello(loud)


#2

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)     # Now divide is a function that divides by 2
print(divide(10))       # Output: 5.0
