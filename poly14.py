class User:
    def __init__(self,name):
        self.name=name
class Admin(User):
    def __init__(self,name,role):
        super().__init__(name)
        self.role=role
a=Admin("Riya","Admin")
print(a.name,a.role)