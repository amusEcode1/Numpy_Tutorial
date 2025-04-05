import numpy as np
print('Add the Elements of three lists')
w = [0,1,2,3]
x = [4,5,6,7]
y = [8,9,10,11]
z = []
for i, j, k in zip(w, x, y):
    z.append(i + j + k)
print(z)

w = [0,1,2,3]
x = [4,5,6,7]
y = [8,9,10,11]
z = np.add(w, x)
result = np.add(z, y)
print(result)