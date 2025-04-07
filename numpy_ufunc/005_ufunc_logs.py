from math import log
import numpy as np
print('NumPy Logs => Log base 2')
arr = np.arange(1, 9)
result = np.log2(arr)
print(result)

print('\nNumPy Logs => Log base 10')
arr = np.arange(1, 11)
result = np.log10(arr)
print(result)

print('\nNumPy Logs => Log base e')
arr = np.arange(1, 10)
result = np.log(arr)
print(result)

print('\nNumPy Logs => Log at any base')
nlog = np.frompyfunc(log, 2, 1)
print(nlog(340, 13)) # 13 is the base