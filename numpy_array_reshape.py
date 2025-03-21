import numpy as np
#Reshapping means changing the shape of an array
print('Reshape from 1-D to 2-D')
arr = np.array([1,2,3,4,5,6,7,8,9])
arr_reshape = arr.reshape(3,3) #multipying both the rows and colums must give the number of the original array
print(arr_reshape, '\n')

print('Reshape from 1-D to 3-D')
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr_reshape1 = arr.reshape(3,2,2) #multipying both the depth, rows and colums must give the number of the original array
arr_reshape2 = arr.reshape(2,3,2)
print(arr_reshape1, '\n')
print(arr_reshape2, '\n')

print('Reshape from 2-D to 3-D')
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr_reshape = arr.reshape(2,2,3)
print(arr_reshape, '\n')

print('Reshape from 2-D to 1-D')
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr_reshape = arr.reshape(-1)
print(arr_reshape, '\n')

print('Reshape from 3-D to 1-D')
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr_reshape1 = arr.reshape(-1)
#OR
arr_reshape2 = arr.ravel() #ravel() converts an array into 1-D Array => It returns view
#OR
arr_reshape3 = arr.flatten() #flatten() converts an array into 1-D Array => It returns copy
#Run the code to see the effects of copy and view
arr_reshape2[0] = 77
arr_reshape3[0] = 99
print(arr_reshape1) #the view() changes its 1st element to 77 => changes made to the view, affects the array and vice versa
print(arr_reshape2) 
print(arr_reshape3, '\n') 

print('Reshape from 3-D to 2-D')
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr_reshape = arr.reshape(4,3)
print(arr_reshape, '\n')

print('Unknown Dimension') 
arr1 = np.array([1,2,3,4,5,6,7,8])
arr2 = np.array([0,1,2,3,4,5,6,7,8,9,10,33,34,35,36,37])
arr3 = np.array([0,1,2,3,4,5,6,7,8,9])
unknown_Dimension1 = arr1.reshape(2,2,-1) # -1 makes in unknown => automatically finds what multipliers to give the number of array
unknown_Dimension2 = arr2.reshape(4,2,-1)
#unknown_Dimension3 = arr3.reshape(2,2,-1) => gives an error, 3 numbers (2,2,?) can't be multiplied to give the number of element of the array (arr3)
print(unknown_Dimension1, '\n')
print(unknown_Dimension2, '\n')

print('Returns Copy or View')
arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr_reshape = arr.reshape(2,5)
print(arr_reshape.base)