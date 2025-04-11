import numpy as np
print('Array Slicing of 1-D Array')
arr = np.array([3,6,7,3,9,2])
print(arr[0:4])
print(arr[1:])
print(arr[:3])
print(arr[-4 : -1])

print('\n Array Slicing of 2-D Array')
arr = np.array([[5,7,6,4],[1,2,3,6]])
print(arr[0, 0:2])
print(arr[1, :1])

print('\n Array Slicing of 3-D Array')
arr = np.array([[[4,5,6,7],[2,3,4,6]],[[3,4,5,7],[2,3,7,8]]])
print([arr[:, 1, 2]])
#To print out the whole Element
print([arr[:,:,:]])

#STEP => to determine the step of the Slicing
print('\n Positive STEP, STEP > 0')
print('Positive step of 1-D Array')
arr = np.array([4,5,6,7,8,9])
print(arr[1:4:2]) #STEP (2) => Moving forward to pick every 2nd Element
print(arr[::1])

print('\nPositive step of 2-D Array')
arr = np.array([[6,4,6,3],[7,3,4,5],[7,2,4,5]])
print(arr[:, ::2])

print('\nPositive step of 3-D Array')
arr = np.array([[[6,4,6,3],[7,3,4,5]],[[7,2,4,5],[2,3,6,8]]])
print(arr[:, :, ::3])

print('\nNegative STEP, STEP < 0')
print('Negative step of 1-D Array')
arr = np.array([2,3,4,5,6,7,8,9])
print(arr[::-2]) #STEP (-2) => Moving backword to pick every 2nd Element
print(arr[::-1])
print(arr[7:1:-1]) #Moving backword to pick all element starting at index 7 & end at index 1

print('\nNegative step of 2-D Array')
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr[::-1, :])
print(arr[:, ::-1])

print('\nNegative step of 3-D Array')
arr = np.array([[[4,5,3,7],[2,1,4,6]],[[8,4,5,7],[2,5,7,8]],[[3,7,2,9],[2,1,7,5]]])
print(arr[::-2, :, :])
print(arr[:, ::-1, ::-2])
