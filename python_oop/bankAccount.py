# Assignment: BankAccount
# Objectives
# Practice writing classes

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class BankAccount:
  def __init__(self, int_rate, balance):
    self.int_rate = 1.01
    self.balance = 0

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    self.balance -= amount
    return self

  def display_account_info(self):
    print("Balance:", "$",self.balance)    
    
  def yield_interest(self):
    self.balance *= self.int_rate
    return self

bank1 = BankAccount(1.01,0)
bank1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

bank2 = BankAccount(1.01,0)
bank2.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()
