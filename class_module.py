class Car:

    def __init__(self,make,model,year,color):
        # class car attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    #object class methods for the car
    def drive(self):
        print("This " + self.model +" is driving")
    def stop(self):
        print("This"+self.model + " is stopped")

#  Summary Rules:
# ✅ Use attributes to store information (nouns).
#
# ✅ Use methods to do actions (verbs).
#
# 💡 Think: "What does this object have?" → attribute
#
# 💡 Think: "What can this object do?" → method


# | Term         | Meaning                                                        |
# | ------------ | -------------------------------------------------------------- |
# | `class`      | Blueprint for creating objects                                 |
# | `__init__()` | Constructor method (runs when object is created)               |
# | `self`       | Refers to the current object                                   |
# | Attributes   | Variables like `make`, `model`, tied to the object             |
# | Methods      | Functions like `drive()` and `stop()` defined inside the class |
#

# car_1=Car("shevy","corvette",2021,"blue")
# print(car_1.make)
# print(car_1.color)
# print(car_1.year)
# print(car_1.model)
#
# car_1.drive()
# car_1.stop()