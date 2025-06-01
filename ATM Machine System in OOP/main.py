from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance


    def get_balance(self):
      return self.__balance

    def set_balance(self, amount):
      self.__balance = amount


    @abstractmethod
    def deposit(self, amount):
      pass

    @abstractmethod
    def withdraw(self, amount):
      pass

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance()  - amount)
            print(f"{self.account_holder} withdrew {amount}. Remaining balance is {self.get_balance()}")

        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.set_balance(self. get_balance() + amount)  

        print(f"{self.account_holder} deposit {amount}. New balance is {self.get_balance()}")

class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f"{self.account_holder} deposit {amount}. New balance is {self.get_balance()}")

        else:
            print("Insufficient balance  in current account")

    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount) 
        print(f"{self.account_holder} deposit {amount}. New balance is {self.get_balance()}")

user1 =SavingsAccount("Mustufa", 1000)  
user1.deposit(500)  
user1.withdraw(200)

user2=CurrentAccount("Anabia", 2000)
user2.deposit(1000)
user2.withdraw(500)






        