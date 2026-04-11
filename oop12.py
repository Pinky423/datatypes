class animal:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Animal name:",self.name)
a=animal("Buffellow")
a.display()
