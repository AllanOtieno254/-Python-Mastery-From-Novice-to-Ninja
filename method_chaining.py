# method_chaining: calling multiple methods sequentially
#                     each call performs an action on the same object and return self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("you drive the car")
        return self

    def brake(self):
        print("You step on the break")
        return self

    def turn_of(self):
        print("you turn off the engine")
        return self

car=Car()
# car.turn_on()
# car.drive()
car.turn_on().drive().brake().turn_of()