class Car:

    color=None

def change_color(car,color):
    car.color=color

car_1=Car()
car_2=Car()

change_color(car_2,"red")
change_color(car_1,"green")

print(car_2.color)
print(car_1.color)