from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        l, w = 4, 3
        print("Rectangle Area:", l * w)

class Circle(Shape):
    def area(self):
        r = 5
        print("Circle Area:", 3.14 * r * r)

r = Rectangle()
c = Circle()

r.area()
c.area()