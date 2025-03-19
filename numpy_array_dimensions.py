import numpy as np
#0 Dimensional Array
arr_0D = np.array(67)

#1 Dimensional Array
arr_1D = np.array([3,7,4,9])

#2 Dimensional Array
arr_2D = np.array([[5,2,4],[3,9,7]])

#3 Dimensional Array
arr_3D = np.array([[[4,7,8],[6,2,1]],[[1,2,3],[7,3,5]]])

#Print out each arrays
print('0-D Array: ', arr_0D)
print('1-D Array: ', arr_1D)
print('2-D Array: ', arr_2D)
print('3-D Array: ', arr_3D)

#To check the number of dimensions => ndim
print(f'{arr_0D.ndim} Dimension')
print(f'{arr_1D.ndim} Dimension')
print(f'{arr_2D.ndim} Dimension')
print(f'{arr_3D.ndim} Dimension')

#Higher Dimensional Array => ndmin
arr = np.array([6,6,7,8,3],ndmin=10)
print('Number of Dimension: ', arr)
'''print('OR')
print(f'Number of Dimension: {arr}')'''
