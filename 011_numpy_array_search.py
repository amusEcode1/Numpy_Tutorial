import numpy as np
print('Searching Arrays => where()')
arr = np.array([1,2,3,4,5,6,7])
result = np.where(arr == 2)
print(result)

arr = np.array([1,2,3,3,7,6,6,3,9,3])
result = np.where(arr == 3)
print(result)

print('\nFind the even numbers in the array')
arr = np.array([1,2,3,4,5,6,7,8,9,10])
result = np.where(arr % 2 == 0)
print(result)

print('\nFind the odd numbers in the array')
arr = np.array([1,2,3,4,5,6,7,8,9,10])
result = np.where(arr % 2 == 1)
print(result)

print('\n Search Sorted => searchsorted()')
arr = np.array([1,3,5,7,8,9])
result = np.searchsorted(arr, 9)
print(result)

print('\n search from the right side')
arr = np.array([4,5,6,7,8,9])
result = np.searchsorted(arr, 6, side = 'right')
print(result)

print('\nSearch for multiple values')
arr = np.array([2,4,6,9])
result = np.searchsorted(arr, [1,3,7])
print(result)

print('\nMultiple values without duplicate')
arr = np.array([2,4,6,9])
result1 = np.searchsorted(arr, [1,3,7], side = 'right')
result2 = np.searchsorted(arr, [1,3,7], side = 'right')
print(f'Left: {result1}')
print(f'Right: {result2}')

print('\nMultiple values with duplicate')
arr = np.array([1,2,2,2,3,3,4,6,6,7,9])
result1 = np.searchsorted(arr, [1,3,7], side = 'left') #default
result2 = np.searchsorted(arr, [1,3,7], side = 'right')
print(f'Left: {result1}')
print(f'Right: {result2}')
