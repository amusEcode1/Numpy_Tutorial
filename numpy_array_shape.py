import numpy as np
#Get the shape of any Array
print('Shape of 1 - Dimensional Array')
arr_1D = np.array([1,2,3,4,5,6])
print(arr_1D.shape, '\n')

print('Shape of 2 - Dimensional Array')
arr_2D = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #the rows and columns of each array, must be unique.
print(arr_2D.shape, '\n')

print('Shape of 3 - Dimensional Array')
arr_3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #the rows and columns of the depth, must be unique.
print(arr_3D.shape, '\n')

#If you need different rows and columns, use a list of arrays instead.
arr = [np.array([[1,2],[3,4]]), np.array([[5,6,7],[8,9,10]])]
print(arr, '\n')

#Let create an array with 10 dimensions
arr_10D = np.array([1,2,3,4,5], ndmin = 10)
print(arr_10D.shape)

#Play around the code using other datatypes...