# duck_typing:concept where the class of an object is less important than the methods
#             class type is not checked if minimum method/attributes are present
#             "if it walks like a duck and it quacks like a duck then it must be a duck"



class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quarking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is talking")

class Person:
    def catch(self,duck):
        duck.walk() #example if we remove duck.walk() from either chicken/duck in their method then create object person.catch(duck) it wont work
                    #this will assume that the catch that the chjicken or duck doesnt have the properties to be taken from
        duck.talk()
        print("You caught the critter")

duck=Duck()
chicken=Chicken()
person=Person()

print("\n")
duck.talk()
duck.walk()

print("\n")
person.catch(duck)

print("\n")
chicken.walk()
chicken.talk()
