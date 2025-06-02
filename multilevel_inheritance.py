# multi_level inheritance: when a derived(child) class inherits another derived(child) class

class organism:
    alive=True

class Animal(organism):
    def eat(self):
        print("This animal is eating")

class dog(Animal):
    def bark(self):
        print("This animal is a dog and so it barks")

dog=dog()
print(dog.alive)
dog.eat()
dog.bark()