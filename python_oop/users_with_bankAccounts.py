# Assignment: Users with Bank Accounts
# Objectives:
# Practice writing classes with associations

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account = BankAccount(int_rate=0.02, balance=0)
  
  def make_deposit(self, amount):
    self.account.deposit(amount)	
    #print(self.account.balance)
    return self
  
  def make_withdraw(self, amount):
    self.account.withdraw(amount)	
    #print(self.account.balance)
    return self
  
  def display_user_balance(self):
    print("Balance:", "$", self.account.balance)
    return self
 
class BankAccount:
  def __init__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    return self
  
  def withdraw(self, amount):
    self.balance -= amount
    return self

guido = User("Guido van Rossum", "guido@python.com")
guido.make_deposit(100).make_withdraw(50).display_user_balance()
