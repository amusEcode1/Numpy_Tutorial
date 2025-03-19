import numpy as np
#1-D Array Indexing
print('Array Indexing of 1-D Array')
arr_1D = np.array([7,3,5,1])
print(arr_1D[0])
print(f'Sum of the 2nd and the 4th Element: {arr_1D[1] + arr_1D[3]} \n')
#2-D Array Indexing
print('Array Indexing of 2-D Array')
arr_2D = np.array([[4,6,2],[9,3,5]])
print(f'3rd Element on 1st row: {arr_2D[0 , 2]}')
print(f'{arr_2D[0 , 2] + arr_2D[1 , 1]} \n')
#3-D Array Indexing
print('Array Indexing of 3-D Array')
arr_3D = np.array([[[3,6,7,8],[5,2,3,4]],[[5,2,3,4],[7,1,2,3]],[[1,2,3,4],[2,3,4,5]],[[6,7,8,7],[6,2,3,4]]])
print(f'3rd Element on 2nd row in the 1st depth: {arr_3D[0, 1, 2]}')
print(f'{arr_3D[0 , 1, 3] + arr_3D[3 , 0, 2]}\n')
#Negative Indexing: To access an Array/Element from the end
print('Negative Indexing')
#1-D Negative Array Indexing
arr_1D_negArr = np.array([7,3,5,1])
print(arr_1D_negArr[-1])
#2-D Negative Array Indexing
arr_2D_negArr = np.array([[4,6,2],[9,3,5]])
print(arr_2D_negArr[-1, 0])
print(arr_2D_negArr[0, -1])
#3-D Negative Array Indexing
arr_3D_negArr = np.array([[[3,6,7,8],[5,2,3,4]],[[5,2,3,4],[7,1,2,3]]])
print(arr_3D_negArr[-1,0,3])