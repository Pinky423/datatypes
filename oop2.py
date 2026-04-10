class counter:
    def __init__(self):
        self.count=0
    def increment(self):
        self.count+=1
    def display(self):
        print("count:",self.count)
c=counter()
c.increment()
c.display()
