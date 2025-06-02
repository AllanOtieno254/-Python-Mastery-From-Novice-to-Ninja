# super():function used to give access to the method of a parent class
#         returns a temporary object of a parent class when used


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class square(Rectangle):
    # def __init__(self,length,width):
    #     self.length=length
    #     self.width=width
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class cube(Rectangle):
    # def __init__(self,length,width,height):
    #     self.length=length
    #     self.width=width
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = square(3, 3)
cube = cube(2, 4, 6)

print(square.area())
print(cube.volume())


