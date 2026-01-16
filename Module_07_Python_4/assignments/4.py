from abc import ABC, abstractmethod


class Shape:
    def __init__(self, shapeName):
        self.shapeName = shapeName
    @abstractmethod
    def area():
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.141
    
class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
    def area(self):
        return self.side * self.side
    
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

shapesList = [Circle(1), Square(4), Triangle(10, 10)]
for shape in shapesList:
    print(f"Area of {shape.shapeName} = {shape.area()} cm^2")