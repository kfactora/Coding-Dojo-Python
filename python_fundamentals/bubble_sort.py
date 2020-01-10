# Bubble Sort
# Objectives:
# Execute the famous Bubble Sort

arr = [6,5,3,1,8,7,2,4]

def bubleSort(arr):
  for j in range(len(arr)-1):
    for i in range(len(arr)-1-j):
       if arr[i] > arr[i+1]:
          arr[i], arr[i+1] = arr[i+1], arr[i]
  return arr
print(bubleSort(arr))
