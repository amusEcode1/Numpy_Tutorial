import numpy as np
print('Simple Arithmetic => Addition')
arr1 = np.array([0,1,2,3,4,5])
arr2 = np.array([6,7,8,9,10,11])
result = np.add(arr1, arr2)
print(result)

print('\nSimple Arithmetic => Subtraction')
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([25,20,50,90,10])
result = np.subtract(arr1, arr2)
print(result)

print('\nSimple Arithmetic => Multiplication')
arr1 = np.array([0,1,2,3,4,5])
arr2 = np.array([6,7,8,9,10,11])
result = np.multiply(arr1, arr2)
print(result)

print('\nSimple Arithmetic => Division')
arr1 = np.array([6,1,2,3,4,5])
arr2 = np.array([6,7,8,9,10,11])
result = np.divide(arr2, arr1)
print(result)

print('\nSimple Arithmetic => Power')
arr1 = np.array([0,1,2,3,4,5])
arr2 = np.array([6,7,8,9,10,11])
result = np.power(arr1, arr2)
print(result)

print('\nSimple Arithmetic => Remainder')
arr1 = np.array([6,1,2,3,4,5])
arr2 = np.array([6,7,8,9,10,11])
result1 = np.remainder(arr2, arr1) # Both remainder and mod are the same
result2 = np.mod(arr2, arr1)
print(result1)
print(result2)

print('\nSimple Arithmetic => Power')
arr1 = np.array([0,1,2,3,4,5])
arr2 = np.array([6,7,8,9,10,11])
result = np.power(arr1, arr2)
print(result)

print('\nSimple Arithmetic => Quotient & Mod')
arr1 = np.array([6,7,8,9,10,11])
arr2 = np.array([6,1,2,3,4,5])
result = np.divmod(arr1, arr2) # from the outputs, the first array represents the quotients & the second array represents the remainder
print(result)

print('\nSimple Arithmetic => Absolute')
arr = np.array([1, -2, -3, 4, -5, 6, -7])
result = np.absolute(arr)
print(result)