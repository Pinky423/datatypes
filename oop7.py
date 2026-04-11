
class Students:
    def __init__(self,name,m1,m2,m3):
        self.__name=name
        self.__marks=[m1,m2,m3]
    def average(self):
        return sum(self.__marks)/3
        
    def grade(self):
        avg=self.average()
        if avg>=75:
            return "A"
        if avg>=50:
            return "B"
        else:
            return "c"
    def display(self):
        print("name:",self.__name)
        print("average:",self.average())
        print("grade:",self.grade())
s=Students("rahul",67,87,56)
s.display()