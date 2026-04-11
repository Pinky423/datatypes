class Account:
    def __init__(self):
        self.__balance=0
    def deposit(self,amt):
        self.__balance+=amt
    def withdraw(self,amt):
        if amt<=self.__balance:
            self.__balance-=amt
        else:
            print("Sufficient amount")
    def show(self):
        print("Amount:",self.__balance)
a=Account()
a.deposit(4000)
a.withdraw(1800)
a.show()

