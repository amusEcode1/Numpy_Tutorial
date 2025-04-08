import numpy as np
print('NumPy Differences')
arr = np.array([2,10,4,14])
result = np.diff(arr)
print(result)

arr1 = np.array([2,10,4,14])
arr2 = np.array([34,13,4,8])
result1 = np.diff([arr1, arr2])
result2 = np.diff([arr1, arr2], axis = 0)
result3 = np.diff([arr1, arr2], axis = 1)
print(result1)
print(result2)
print(result3)

print('\nNumPy Differences => Discrete Difference')
arr = np.array([2,10,4,14])
result1 = np.diff(arr, n = 1) # n = 1 is the default value
result2 = np.diff(arr, n = 2) # finds the difference twice
result3 = np.diff(arr, n = 3) # finds the difference trice
print(result1)
print(result2)
print(result3)