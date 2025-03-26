import numpy as np
#0 Dimensional Array
arr1 = np.array(67)

#1 Dimensional Array
arr2 = np.array([3,7,4,9])

#2 Dimensional Array
arr3 = np.array([[5,2,4],[3,9,7]])

#3 Dimensional Array
arr4 = np.array([[[4,7,8],[6,2,1]],[[1,2,3],[7,3,5]]])

#Print out each arrays
print('0-D Array: ', arr1)
print('1-D Array: ', arr2)
print('2-D Array: ', arr3)
print('3-D Array: ', arr4, '\n')

#To check the number of dimensions => ndim
print(f'{arr1.ndim} Dimension')
print(f'{arr2.ndim} Dimension')
print(f'{arr3.ndim} Dimension')
print(f'{arr4.ndim} Dimension\n')

#Higher Dimensional Array => ndmin
arr = np.array([6,6,7,8,3],ndmin=10)
print('Number of Dimension: ', arr)
'''print('OR')
print(f'Number of Dimension: {arr}')'''
