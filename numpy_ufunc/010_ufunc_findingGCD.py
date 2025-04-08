import numpy as np
print('Finding GCD => Greatest Common Divisor')
x = 12
y = 15
result = np.gcd(x, y)
print(result)

print('\nFinding GCD in Arrays')
arr1 = np.array([4, 16, 40, 56])
arr2 = np.arange(1, 11)
result1 = np.gcd.reduce(arr1)
result2 = np.gcd.reduce(arr2)
print(result1)
print(result2)