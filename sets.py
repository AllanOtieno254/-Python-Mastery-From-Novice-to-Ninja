# set: collection which is unordered,unindexed.No duplicate values

utensils={"fork","spoon","knife","knife","knife"}
dishes={"bowl","plate","cup","fork"}


for x in utensils:
    print(x)

print("\n")

#methods in set
utensils.add("napkins")
utensils.remove("fork")
for x in utensils:
    print(x)

print("\n")
utensils.update(dishes)
for x in utensils:
    print(x)

print("\n")
dinner_table=utensils.union(dishes)
for x in utensils:
    print(x)

print("\n")
print(utensils.difference(dishes))

print("\n")
print(utensils.intersection(dishes))