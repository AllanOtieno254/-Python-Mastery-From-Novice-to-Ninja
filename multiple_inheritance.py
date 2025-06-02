# multiple_inheritance:when a child class is derived from more than one parent class
from inheritance import rabbit


class prey:
    def flee(self):
        print("The animal flees")

class predator:
    def hunt(self):
        print("The animal is hunting")


class Rabbit(prey):
    pass
class Hawk(predator):
    pass
class fish(prey,predator):
    pass

#creating object
rabbit=Rabbit()
hawk=Hawk()
fish=fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()