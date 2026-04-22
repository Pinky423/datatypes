class Calculator:
    def Multiply(self,a,b,c=1):
        return a*b*c
c=Calculator()
print(c.Multiply(3,4))
print(c.Multiply(2,4,3))