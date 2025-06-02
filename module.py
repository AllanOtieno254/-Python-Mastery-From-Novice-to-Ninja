# module: a file containing python code,may contain functions,classes etc.
#         used with modular programming,which is to separate a program into parts

import module2 #as mod----this is just adding an alias to shorten instead of using whole name module2 you use mod

#to use  the function in module2 type name of module.name of function
module2.hello()
module2.bye()


print("\n")
# alternative
from module2 import hello,bye
hello()
bye()

#if you want to access python modules use
help("modules")