# Assignment: MathDojo
# Objectives:
# Practice creating a class and creating new instances
# Practice chaining methods
# Practice writing flexible functions that can take a varying number of arguments
#Create a Python class called MathDojo that has one attribute, result, and 2 methods: add and subtract. The 2 methods each must take at least 1 parameter, but could take many more.

class MathDojo(object):
	def __init__(self): 
		self.total = 0

	def add(self, *num): 
		for i in range(0, len(num)):
			if type(num[i]) is list or type(num[i]) is tuple:
				for j in num[i]: 
					self.total += j
			else:
				self.total += num[i]
		return self 

	def subtract(self, *num): 
		for i in range(0, len(num)):
			if type(num[i]) is list or type(num[i]) is tuple:
				for j in num[i]: 
					self.total -= j
			else:
				self.total -= num[i]
		return self

	def result(self): 
		print(self.total)

md = MathDojo().add([1],2,3).add([4, 5, 6, 7], [8, 9.10, 11.12]).result()
