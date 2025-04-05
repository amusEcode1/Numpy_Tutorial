import numpy as np
print('Rounding Decimals => Truncation')
arr = np.array([-4.1223, 2.7789, -1.437])
result = np.trunc(arr)
print(result)

print('\nRounding Decimals => Fix')
arr = np.array([-4.1223, 2.7789, -1.437])
result = np.fix(arr)
print(result)

print('\nRounding Decimals => Round')
arr = np.array([-4.1223, 2.7789, -1.437])
result1 = np.around(arr)
result2 = np.around(arr, 3)
result3 = np.around(2.7789, 2)
print(result1)
print(result2)
print(result3)

print('\nRounding Decimals => Floor')
arr = np.array([-4.1223, 2.7789, -1.437])
result = np.floor(arr)
print(result)

print('\nRounding Decimals => Ceil')
arr = np.array([-4.1223, 2.7789, -1.437])
result = np.ceil(arr)
print(result)