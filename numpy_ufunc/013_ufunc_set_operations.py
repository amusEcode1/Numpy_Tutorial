import numpy as np
print('Set => Create Sets in NumPy')
arr = np.array([2,4,5,8,9,9,9,0,5,1,1,3,7])
result = np.unique(arr)
print(result)

print('\nSet => Finding Union')
arr1 = np.array([2,3,4,1,1])
arr2 = np.array([5,7,6,8])
result = np.union1d(arr1, arr2) # unique values of the 2 arrays
print(result)

print('\nSet => Finding Intersection')
arr1 = np.array([2,3,4,1,1])
arr2 = np.array([5,2,1,1,8,4,7,6,8])
result = np.intersect1d(arr1, arr2) # values present in both arrays
print(result)

print('\nSet => Finding Difference')
arr1 = np.array([2,3,4,1,1])
arr2 = np.array([5,2,1,1,8,4,7,6,8])
result = np.setdiff1d(arr1, arr2)
print(result)

print('\nSet => Finding Difference')
arr1 = np.array([2,3,4,1])
arr2 = np.array([5,2,1])
result = np.setdiff1d(arr1, arr2, assume_unique = True)
print(result)

print('\nSet => Symmetric Difference')
arr1 = np.array([2,3,4,1])
arr2 = np.array([5,2,1])
result = np.setxor1d(arr1, arr2, assume_unique = True)
print(result)
