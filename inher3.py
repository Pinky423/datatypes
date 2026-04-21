class Grandparent:
    def show1(self):
        print("Grandparent")
class Parent(Grandparent):
    def show2(self):
        print("Parent")
class Child(Parent):
    def show3(self):
        print("child")
c= Child()
c.show1()
c.show2()
c.show3()