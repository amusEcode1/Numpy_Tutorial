import numpy as np
# Sort() returns copy of an array without changing the original array
print('Sorting 1-D Array Arrays')
arr = np.array([5,3,4,6,7,1,2,9,8])
result = np.sort(arr)
print(result)

arr = np.array(['amusEcode', 'Becky', 'hannah']) #It checkes the capitalized letter first
result = np.sort(arr)
print(result)

arr = np.array([True, False, False, True]) #False => 0 and True => 1
result = np.sort(arr)
print(result)

print('\nSorting 2-D Array Arrays')
arr = np.array([[3,1,2],[4,6,5]])
result = np.sort(arr)
print(result)

print('\nSorting 3-D Array Arrays')
arr = np.array([[[3,2,1],[5,6,4]],[[7,8,9],[12,11,10]]])
result = np.sort(arr)
print(result)

print('\nusing sort() to find the even numbers in a 3-D unsorted array')
arr = np.array([[[3,2,1],[5,6,4]],[[7,8,9],[12,11,10]]])
result1 = np.sort(arr)
result2 = np.where(result1 % 2 == 0)
print(result2)
