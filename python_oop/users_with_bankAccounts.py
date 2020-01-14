# Assignment: Users with Bank Accounts
# Objectives:
# Practice writing classes with associations

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account = BankAccount(int_rate=0.02, balance=0)
  
  def example_method(self, amount):
    self.account.deposit(amount)	
    print(self.account.balance)
    return self
 
class BankAccount:
  def __init__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    return self

guido = User("Guido van Rossum", "guido@python.com")
guido.example_method(100)
