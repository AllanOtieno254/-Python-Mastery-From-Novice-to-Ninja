# reduce(): apply a function to an iterable and reduces it to a single cumulative value.
#             performs function on first two elements and report process until 1 value remains
#
# reduce(function,iterable)

import functools

letters=["H","E","L","L","O"]
word=functools.reduce(lambda x,y:x+y,letters)
print(word)

#finding factorial of 5
factorial=[5,4,3,2,1]
result=functools.reduce(lambda x,y:x*y,factorial)
print(result)