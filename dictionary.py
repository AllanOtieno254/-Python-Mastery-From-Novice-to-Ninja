# dictionary: a changable,unordered collection of unique key:vslue pairs
#             fast because they use hashing ,allow us to access a value quickly

capitals={"USA":"Washington DC",
          "India":"New Dehli",
          "China":"Beijing",
          "Russia":"Moscow"}

print(capitals)

print(capitals["USA"])

#checking if theres a key
print(capitals.get("Germany"))

#printing only keys without values
print(capitals.keys())

#printing only values without keys
print(capitals.values())

print(capitals.items())

print("\n")
for key,value in capitals.items():
    print(key,value)

print("\n")
capitals.update({"India":"Berlin"})
print(capitals["India"])
for key,value in capitals.items():
    print(key,value)

capitals.pop("China")
capitals.clear()







