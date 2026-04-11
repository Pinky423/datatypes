class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person("Aman", 20)
p2 = Person("Riya", 22)

p1.display()
p2.display()
