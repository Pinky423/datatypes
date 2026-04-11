class person:
    def __init__(self):
        self.__age=0
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Inavalid age")
    def get_age(self):
        return self.__age
p=person()
p.set_age(20)
print(p.get_age())