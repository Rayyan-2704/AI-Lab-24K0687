class BankAccount:
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive!")
        else:
            self.__balance += amount
            print(f"${amount} has been deposited to account {self.account_number}.\nNew Balance: ${self.__balance}")
            
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
        elif self.__balance < amount:
            print("Error: Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"${amount} has been withdrawn from account {self.account_number}.\nNew balance: ${self.__balance}")
            
    def get_balance(self):
        return self.__balance
    
def main():
    account1 = BankAccount("Rayyan Aamir", "B-1001", 2500)
    account2 = BankAccount("Murtaza Hunaid", "B-1002", 5000)
    account3 = BankAccount("Hammad Haider", "B-1003", 3450)
    
    account1.deposit(400)
    account1.withdraw(1000)
    print()
    
    account2.deposit(2000)
    account2.withdraw(10000)
    print()
    
    account3.withdraw(250)
    account3.deposit(700)
    
    print("\n--------- Account 1 ---------")
    print(f"Holder Name: {account1.name}")
    print(f"Account Number: {account1.account_number}")
    print(f"Balance: ${account1.get_balance()}")
    
    print("\n--------- Account 2 ---------")
    print(f"Holder Name: {account2.name}")
    print(f"Account Number: {account2.account_number}")
    print(f"Balance: ${account2.get_balance()}")
    
    print("\n--------- Account 3 ---------")
    print(f"Holder Name: {account3.name}")
    print(f"Account Number: {account3.account_number}")
    print(f"Balance: ${account3.get_balance()}")
    
main()