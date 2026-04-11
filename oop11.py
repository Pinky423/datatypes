class person:
    def __init__(self,name):
        self.name=name
        print(self.name,"create")
    def __del__(self):
        print(self.name,"delete")
p=person("Hello pinky")
del p