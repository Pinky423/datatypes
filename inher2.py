class Teacher:
    def teach(self):
        print("Teaching")

class Administrator:
    def manage(self):
        print("Managing")

class Headmaster(Teacher, Administrator):
    pass

h = Headmaster()
h.teach()
h.manage()