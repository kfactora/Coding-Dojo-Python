# Assignment: User
# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account_balance = 0
  
  def make_deposit(self, amount):	
    self.account_balance += amount
  def make_withdrawal(self, amount):	
    self.account_balance -= amount

  def display_balance(self):	
    print("Name:",self.name)
    print("Balance:",self.account_balance)
  
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(200)
guido.make_withdrawal(100)
guido.display_balance()
monty.display_balance()
