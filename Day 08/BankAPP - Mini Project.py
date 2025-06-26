#BankAPP - Mini Project    
class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount} and new balance ${self.__balance}.")
        
    def withdrew(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print(f"withdrew ${amount} and new Balance ${self.__balance}.")
            
    def show(self):
        print(f"{self.name}'s account balance is ${self.__balance}.")
B = BankAccount("Ganesh", 10000)
B.deposit(5000)
B.withdrew(500)
B.show()