class Transport:
    def travel(self):
        pass

class Train(Transport):
    def travel(self):
        print("Travel by Train")

class Plane(Transport):
    def travel(self):
        print("Travel by Plane")

t = Train()
p = Plane()

t.travel()
p.travel()