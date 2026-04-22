class Printer:
    def print_data(self, a=None, b=None):
        if a and b:
            print(a, b)
        else:
            print(a)

p = Printer()
p.print_data("Hello")
p.print_data(10)
p.print_data("Hi", 20)