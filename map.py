# map(): applies a function to each item in an iterable(list,tuple et)
#
# map(function,iterable)

#converting the amount of the items i store to euros by 0.082
store=[("shirt",20.00),
       ("pants",25.00),
       ("jackets",50.00),
       ("socks",10.00)]

to_euros= lambda data:(data[0],data[1]*0.82)
to_dollars= lambda data:(data[0],data[1]/0.82)
# print(to_euros(store[0]))
store_euros=list(map(to_euros, store))
store_dollars=list(map(to_dollars,store))

for i in store_euros:
       print(i)
print("\n")
for i in store_dollars:
       print(i)



print("\n")

friends = [("Allan", 20),
           ("peter", 16),
           ("charity", 19),
           ("Damaris", 17),
           ("kimkim", 15),
           ("sebu", 26)]

drinking_friends = lambda age: "adult" if age[1] >= 18 else "child"
drinking_friends1 = list(map(drinking_friends, friends))

for i in drinking_friends1:
    print(i)

# if you want to include name and filtering if adult or child by specific person use f string
print("\n")
friends_filtering= lambda person: f"{person[0]}:adult" if person[1]>=18 else f"{person[0]}:child"
drinking_friends_map=list(map(friends_filtering,friends))

for i in drinking_friends_map:
    print(i)





