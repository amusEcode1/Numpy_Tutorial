import numpy as np
print('Finding LCM => Lowest Common Multiple')
x = 3
y = 7
result = np.lcm(x, y)
print(result)

print('\nFinding LCM in Arrays')
arr1 = np.array([2, 3, 9, 8, 4])
arr2 = np.arange(1, 10)
result1 = np.lcm.reduce(arr1)
result2 = np.lcm.reduce(arr2)
print(result1)
print(result2)
