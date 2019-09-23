'''
Write  a Python program to emulate a Bank where a customer of the bank can withdraw and deposit money in the bank.
Show the following details using instance variables and class variables:
1. Individual  Bank Balance of customers
2. Total Money in the Bank
3. Perform Deposit and Withdrawal of money from a bank account.
4. A Bank can have multiple customers.
'''

class Bank:
    def __init__(self, name):
        self.name = name
        self.customer = []
    def total_balance(self):
        total = 0
        for i in self.customer:
            total += i.balance
        return total

class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    def display(self):
        return self.balance

bank = Bank("hdfc")
cust_1 = Customer('Sachin',500)
cust_2 = Customer('Varun',1000)
bank.customer.append(cust_1)
bank.customer.append(cust_2)

print(bank.total_balance())
print("Deposit 200 rs, new bank balance", cust_1.deposit(200), bank.total_balance())

# while(1):
#     choice = int(input("Choose your option:\n1.Display balance\n2.Deposit money\n3.Withdraw money\n4.Exit\n"))
#     if choice ==1:
#         print("The bank balance is", customer.display_balance())
#     elif choice == 2:
#         deposit_amount = float(input("Enter your deposit amount: "))
#         print(f"The bank balance after Rs {deposit_amount} deposit is", customer.deposit(deposit_amount))
#     elif choice == 3:
#         withdraw_amount = float(input("Enter your deposit amount: "))
#         print(f"The bank balance after Rs {withdraw_amount} deposit is", customer.withdraw(withdraw_amount))
#     elif choice == 4:
#         break
#     else:
#         print("Invalid entry. Try again")