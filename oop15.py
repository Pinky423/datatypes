class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)
        
s=Students("Pinky",89)
s.display()