class Car2:

    wheels=4 #class variable

    def __init__(self,make,model,year,color):
        self.make=make      #instant variable
        self.model=model    #instant variable
        self.year=year      #instant variable
        self.color=color    #instant variable


car_2=Car2("shevy","audi",2025,"red")
print(car_2.wheels)