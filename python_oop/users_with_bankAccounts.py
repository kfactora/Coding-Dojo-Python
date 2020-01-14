# Assignment: Users with Bank Accounts
# Objectives:
# Practice writing classes with associations

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
  
  def make_deposit(self, amount):
    self.account_balance += amount
    return self
  
  def make_withdrawal(self, amount):	
    self.account_balance -= amount
    return self

  def display_balance(self):	
    print("Name:",self.name)
    print("Balance:",self.account_balance)
  
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
luke = User("Luke Skywalker", "luke@python.com")

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

  def display_account_info(self):
    print("Balance:", "$", self.balance)    
    
  def yield_interest(self):
    self.balance *= self.int_rate
    return self 

bank1 = BankAccount(1.01,0)
bank2 = BankAccount(1.01,0)
