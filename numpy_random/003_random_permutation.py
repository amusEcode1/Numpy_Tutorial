from numpy import random
import numpy as np
print('Shuffling of Arrays')
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

print('\nPermutation of Arrays')
arr = np.array([1,2,3,4,5])
new_arr = random.permutation(arr)
print(arr) # Permutation returns a copy => leaves the original original unchanged
print(new_arr)