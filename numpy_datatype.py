import numpy as np
print('Numpy Data Types')
arr1 = np.array([2,3,4,5,8])
arr2 = np.array(['amusEcode','Becky','Hannah'])
print(arr1.dtype)
print(arr2.dtype, '\n')

print('Creating Arrays with a Defined Data Type')
#Integer (default is int64 or int32 depending on the system)
arr1 = np.array([2,3,4,5,8], dtype = 'i4')
arr2 = np.array([2,3,4,5,8], dtype = np.int32)
arr3 = np.array([255,3,4,5,8], dtype = 'S')
print(arr1.dtype)
print(arr2)
print(arr3)
print(arr3.dtype, '\n')

#String (fixed length byte string)
arr1 = np.array(['amusEcode','Becky','Hannah'])
arr2 = np.array(['amusEcode','Becky','Hannah'], dtype = 'U')
arr3 = np.array(['amusEcode','Becky','Hannah'], dtype = 'S')
arr4 = np.array(['amusEcode','Becky','Hannah'], dtype = 'U5')
arr5 = np.array(['amusEcode','Becky','Hannah'], dtype = 'S5')
print(arr1.dtype)
print(arr2)
print(arr2.dtype)
print(arr3)
print(arr3.dtype)
print(arr4)
print(arr5, '\n')

#Boolean
arr = np.array([False, True, True])
print(arr.dtype, '\n')

#Float
arr1 = np.array([2.5, 66.8, 3.142, 55.8])
arr2 = np.array([2.5, 66.8, 3.142, 55.8], dtype = np.float32)
print(arr1.dtype)
print(arr2.dtype, '\n')

#Complex Float
arr1 = np.array([3-2j, 1+8j, 2+4j])
arr2 = np.array([3-2j, 1+8j, 2+4j], dtype = np.complex64)
print(arr1.dtype)
print(arr2.dtype, '\n')

#Unsigned Integer (Doesn't store negative numbers)
arr = np.array([255,66,4,12,3], dtype = np.uint8)
#arr_uint1 = np.array([255,-66,4,12,3], dtype = np.uint8) Error: Negative sign
print(arr, '\n')

print('Converting Data Type on Existing Arrays => astype()')
#Convert from float to interger
arr = np.array([1.0,2.0,3.0,4.0,5.0])
arr_new = arr.astype('i')
print(arr_new)
print(arr_new.dtype)

arr = np.array([1.0,2.0,3.0,4.0,5.0])
arr_new = arr.astype(int)
print(arr_new)
print(arr_new.dtype, '\n')

#Convert from float to boolean
arr = np.array([0.1,1.0,2.0,3.0,4.0,5.0])
arr_new = arr.astype(bool)
print(arr_new)
print(arr_new.dtype, '\n')

#Convert from integer to boolean
arr = np.array([0,1,2,3,4,5])
arr_new = arr.astype(bool)
print(arr_new)
print(arr_new.dtype, '\n')

#Convert from string to int
arr = np.array(['25', '23', '22']) #Error if the string contains non - integer values
arr_new = arr.astype(int)
print(arr_new, '\n')

#Convert from complex float to boolean
arr = np.array([0-0j, 1+0j, 0+4j, 2+3j, 5-7j])
arr_new = arr.astype(bool)
print(arr_new, '\n')

#Play around the code to convert from one data types to another...
