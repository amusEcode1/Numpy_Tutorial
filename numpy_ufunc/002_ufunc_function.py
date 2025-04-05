import numpy as np
print('Creating ufunc for addition')
def add(x, y):
    return x + y
result = np.frompyfunc(add, 2, 1) # add => name of the function, 2 => inputs(number of input arrays), 1 => outputs(number of output arrays)
print(result([0,1,2,3,4],[5,6,7,8,9]))

def add(x, y, z):
    return x + y + z
result = np.frompyfunc(add, 3, 1) 
print(result([0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]))

print('\ncheck if a function is a ufunc')
print(type(np.add))
print(type(np.sum))
print(type(np.concatenate))

print('\nUsing if statement to check if a function is a ufunc')
if type(np.add) == np.ufunc:
    print('Correct')
else:
    print('Wrong')

print('\nUsing if statement to check if a function is a ufunc')
if type(np.sum) == np.ufunc:
    print('Correct')
else:
    print('Wrong')