class Employee:
    def __init__(self,name):
        self.name=name
        print("employee created")
    def __del__(self):
        print("goodbye",self.name)
e=Employee("Pinky")
del e