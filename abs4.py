
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amt):
        pass

    @abstractmethod
    def withdraw(self, amt):
        pass

class BankAccount(Account):
    def __init__(self, acc_no, balance):
        self.__account_number = acc_no
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, rate):
        super().__init__(acc_no, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.get_balance() * self.rate / 100
        self.deposit(interest)


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, balance, limit):
        super().__init__(acc_no, balance)
        self.limit = limit

    def withdraw(self, amt):
        if amt <= self.get_balance() + self.limit:
            new_balance = self.get_balance() - amt
            self._BankAccount__balance = new_balance  
        else:
            print("Overdraft limit exceeded")

s = SavingsAccount(101, 1000, 10)
c = CurrentAccount(102, 1000, 500)

s.deposit(500)
s.add_interest()
print("Savings Balance:", s.get_balance())

c.withdraw(1200)
print("Current Balance:", c.get_balance())