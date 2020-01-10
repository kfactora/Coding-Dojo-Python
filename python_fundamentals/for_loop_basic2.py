# Assignment: For Loop Basic II
# Objectives:
# Get comfortable writing functions only using basic building blocks of Python (i.e. using your own skills rather than relying on built-ins)
# Get comfortable using for loops, functions, lists, and other data types

# 1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# iterate, i > 0 = 'big', return arr
def biggie_size(arr):
  for i in range(len(arr)):
    if arr[i] > 0:
      arr[i] = "big"
  return arr
print(biggie_size([-1, 3, 5, -5]))

# 2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# iterate, var count, arr[i] > 0 = pos, sum of pos
def count_positives(arr):
  count = 0
  for i in range(len(arr)):
    if arr[i] > 0:
      count += 1
  arr[-1] = count
  return arr
print(count_positives([-1,1,1,1]))

# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
# iterate, var sum, sum of arr
def sum_total(arr):
  count = 0
  for i in range(len(arr)):
    count = count + arr[i]
  return count
print(sum_total([1,2,3,4]))

# 4 Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
# iterate, len(arr) / sum
def average(arr):
  sum = 0
  for i in range(len(arr)):
    sum = sum + arr[i]
  return sum / len(arr)
print(average([1,2,3,4]))

# 5 Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
# iterate, len(arr), return len(arr)
def length(arr):
  return len(arr)
print(length([37,2,1,-9]))

# 6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
# iterate, var min, return min arr[i]
def minimum(arr):
  min = arr[0]
  if len(arr) == 0:
    return False
  for i in arr:
    if i < min:
      min = i
  return min
print(minimum([37,2,1,-9]))

# 7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
# iterate, car max, return max arr[i]
def maximum(arr):
  max = arr[0]
  if len(arr) == 0:
    return False
  for i in arr:
    if i > max:
      max = i
  return max
print(maximum([37,2,1,-9]))

# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
# iterate, combine all
def ultimate_analysis(arr):
  dict = {
    'sumtotal' : sum_total(arr),
    'avg' : average(arr),
    'min' : minimum(arr),
    'max' : maximum(arr),
    'len' : length(arr)
  }
  return dict
print(ultimate_analysis([37,2,1,-9]))

# 9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
# iterate, 
def reversed(arr):
  arr = arr[::-1]
  return arr
print(reverse_list([37,2,1,-9]))
