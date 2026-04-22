from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def area(self):
        l, w = 4, 3
        print("Area:", l*w)

    def perimeter(self):
        l, w = 4, 3
        print("Perimeter:", 2*(l+w))

class Circle(Shape):
    def area(self):
        r = 5
        print("Area:", 3.14*r*r)

    def perimeter(self):
        r = 5
        print("Perimeter:", 2*3.14*r)
        
class Test(Shape):
    def area(self):
        print("Only area")

r = Rectangle()
r.area()
r.perimeter()