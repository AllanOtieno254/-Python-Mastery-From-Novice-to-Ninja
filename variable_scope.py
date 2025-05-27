# scope:the region that a variable is recognized
#         a variable is only available from inside the region its created
#         a global and locally scoped varsion of a variable can be created

# types of scope: local scope and global scope

# local variable_scope

def display_name():
    name="allan otieno"
    return name
print(display_name())

# print(name) : this will not run since its declared as a local variable hence cant be accessed outside the function


#global variable
name="Allano"
print(name)