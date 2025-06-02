# list_comprehension: a way of creating new list with less syntax
#                     can mimic lambda functions, easier to read
#                     list=[expression for item in iterable]

# squares=[]
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)

squares=[i*i for i in range(1,11)]
print(squares)