class shape:
    def area(self):
        pass
class circle(shape):
    def area(self):
        r=5
        print("circle area:",3.14*r*r)
class rectangle(shape):
    def area(self):
        l,w=4,5
        print("Rectangle Area:",l*w)
c=circle()
r=rectangle()
c.area()
r.area()