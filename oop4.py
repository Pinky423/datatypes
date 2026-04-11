class Book:
    def __init__(self):
        self.__title=""
        self.__author=""
    def set_data(self,t,a):
        self.__title=t
        self.__author=a
    def get_data(self):
        print("Title:",self.__title)
        print("Author:",self.__author)
b=Book()
b.set_data("djfs","dwurt")
b.get_data()

