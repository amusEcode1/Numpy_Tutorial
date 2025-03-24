import numpy as np
#Iterating Arrays
print('Iterating 1-D array')
arr = np.array([1,2,3,4,5,6,7,8,9])
for i in arr:
    print(i, '\n')

print('Iterating 2-D arrays')
arr = np.array([[1,2,3,4],[5,6,7,8]])
for i in arr:
    print(i, '\n')

print('Iterating 3-D arrays')
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in arr:
    print(i, '\n')

print('Iterating 2-D arrays in each dimension')
arr = np.array([[1,2,3,4],[5,6,7,8]])
for i in arr:
    for j in i:
        print(j)

print('\nIterating 3-D arrays in each dimension')
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in arr:
    for j in i:
        for k in j:
            print(k)

print('\nIterating 2-D arrays using nditer()')
arr = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(arr):
    print(i)

print('\nIterating 3-D arrays using nditer()')
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in np.nditer(arr):
    print(i)

print('\nIterating array with different data types')
arr = np.array([1,2,3,4,5,6,7,8,9])
for i in np.nditer(arr, flags = ['buffered'], op_dtypes = ['S']):
    print(i)

print('\n Iterating 2-D array with positive step size')
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in np.nditer(arr[:, ::3]):
    print(i)

print('\n Iterating 3-D array with negative step size')
arr = np.array([[[1,2,3]],[[4,5,6]],[[7,8,9]]])
for i in np.nditer(arr[::-1, :, ::-1].copy()): #since it's in non - contiguous format due to slicing ([::-1]), use copy() => reallocates memory in a proper contiguous format, ensuring correct iteration.
    print(i)

print('\n1-D Enumerated Iteration using ndenumerate()')
arr = np.array([1,2,3,4,5,6,7,8,9])
for i, j in np.ndenumerate(arr):
    print(i, j)

print('\n2-D Enumerated Iteration using ndenumerate()')
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
for i, j in np.ndenumerate(arr):
    print(i, j)

print('\n3-D Enumerated Iteration using ndenumerate()')
arr = np.array([[[1,2,3]],[[4,5,6]],[[7,8,9]]])
for i, j in np.ndenumerate(arr):
    print(i, j)