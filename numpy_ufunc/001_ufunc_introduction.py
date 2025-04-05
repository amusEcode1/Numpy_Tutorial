import numpy as np
print('ufuncs => Universal Functions')
print('Add the Elements of three lists => using zip()')
w = [0,1,2,3]
x = [4,5,6,7]
y = [8,9,10,11]
z = []
for i, j, k in zip(w, x, y):
    z.append(i + j + k)
print(z)

print('\nAdd the Elements of three lists => using add()')
w = [0,1,2,3]
x = [4,5,6,7]
y = [8,9,10,11]
z = np.add(w, x)
result = np.add(z, y)
print(result)

print('\nAdd the Elements of three lists => using sum()')
w = [0,1,2,3]
x = [4,5,6,7]
y = [8,9,10,11]
result = np.sum([w, x, y], axis = 0)
print(result)
