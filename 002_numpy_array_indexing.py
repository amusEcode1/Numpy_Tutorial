import numpy as np
#1-D Array Indexing
print('Array Indexing of 1-D Array')
arr = np.array([7,3,5,1])
print(arr[0])
print(f'Sum of the 2nd and the 4th Element: {arr[1] + arr[3]} \n')

#2-D Array Indexing
print('Array Indexing of 2-D Array')
arr = np.array([[4,6,2],[9,3,5]])
print(f'3rd Element on 1st row: {arr[0 , 2]}')
print(f'{arr[0 , 2] + arr[1 , 1]} \n')

#3-D Array Indexing
print('Array Indexing of 3-D Array')
arr = np.array([[[3,6,7,8],[5,2,3,4]],[[5,2,3,4],[7,1,2,3]],[[1,2,3,4],[2,3,4,5]],[[6,7,8,7],[6,2,3,4]]])
print(f'3rd Element on 2nd row in the 1st depth: {arr[0, 1, 2]}')
print(f'{arr[0 , 1, 3] + arr[3 , 0, 2]}\n')

#Negative Indexing: To access an Array/Element from the end
print('Negative Indexing')
#1-D Negative Array Indexing
arr = np.array([7,3,5,1])
a = arr[-1]
b = arr[-3]
print(a, b)
print(f'{a + b} \n')

#2-D Negative Array Indexing
arr = np.array([[4,6,2],[9,3,5]])
print(arr[0, -1])
print(arr[-1, 0])
print(f'The sum of the 2 gives {arr[0, -1] + arr[-1, 0]}\n')

#3-D Negative Array Indexing
arr = np.array([[[3,6,7,8],[5,2,3,4]],[[5,2,3,4],[7,1,2,3]]])
print(arr[-1,0,3])
