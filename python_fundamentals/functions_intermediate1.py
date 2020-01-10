# Assignment: Functions Intermediate I
# Objectives:
# Practice using default parameter values
# Practice passing in named arguments
# Become familiar with Python's random module

# With this concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.

# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.

def randInt(min=0, max=100):
  import random
  num = random.random()*(max-min) + min
  return(int(num))
print(randInt())
print(randInt(min=50, max=50))
print(randInt(min=50, max=100))
print(randInt(min=50, max=200))
