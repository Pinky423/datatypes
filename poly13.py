class Base:
    def display(self):
        print("Base class")
class Derived(Base):
    def display(self):
        super().display()
        print("Derived class")
d=Derived()
d.display()