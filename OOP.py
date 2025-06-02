# class Car: #class name should start with caps
#     pass

from class_module import Car

car_1=Car("shevy","corvette",2021,"blue")
print(car_1.make)
print(car_1.color)
print(car_1.year)
print(car_1.model)

car_1.drive()
car_1.stop()

print("\n")

from class_variable2 import Car2
car_2=Car2("shevy","audi",2025,"red")
#car_2.wheels=5 to overide the called class you can use this
print(car_2.wheels)