class Shape:
    @staticmethod
    def area(a, b=None):
        if b is None:
            return 3.14 * a * a   
        else:
            return a * b         

