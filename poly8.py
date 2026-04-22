class Vehicle:
    def start(self):
        print("Vehicle starts")

class Bike(Vehicle):
    def start(self):
        print("Bike starts")

class Car(Vehicle):
    def start(self):
        print("Car starts")

b = Bike()
c = Car()

b.start()
c.start()