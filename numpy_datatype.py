import numpy as np
print('Numpy Data Types')
arr_int1 = np.array([2,3,4,5,8])
arr_string1 = np.array(['amusEcode','Becky','Hannah'])
print(arr_int1.dtype)
print(arr_string1.dtype, '\n')

#Creating Arrays with a Defined Data Type

#Integer (default is int64 or int32 depending on the system)
arr_int2 = np.array([2,3,4,5,8], dtype = 'i4')
arr_int3 = np.array([2,3,4,5,8], dtype = np.int32)
arr_int4 = np.array([255,3,4,5,8], dtype = 'S')
print(arr_int2.dtype)
print(arr_int3)
print(arr_int4)
print(arr_int4.dtype, '\n')

#String (fixed length byte string)
arr_string2 = np.array(['amusEcode','Becky','Hannah'])
arr_string3 = np.array(['amusEcode','Becky','Hannah'], dtype = 'U')
arr_string4 = np.array(['amusEcode','Becky','Hannah'], dtype = 'S')
arr_string5 = np.array(['amusEcode','Becky','Hannah'], dtype = 'U5')
arr_string6 = np.array(['amusEcode','Becky','Hannah'], dtype = 'S5')
print(arr_string2.dtype)
print(arr_string3)
print(arr_string3.dtype)
print(arr_string4)
print(arr_string4.dtype)
print(arr_string5)
print(arr_string6, '\n')

#Boolean
arr_bool = np.array([False, True, True])
print(arr_bool.dtype, '\n')

#Float
arr_float1 = np.array([2.5, 66.8, 3.142, 55.8])
arr_float2 = np.array([2.5, 66.8, 3.142, 55.8], dtype = np.float32)
print(arr_float1.dtype)
print(arr_float2.dtype, '\n')

#Complex Float
arr_cfloat1 = np.array([3-2j, 1+8j, 2+4j])
arr_cfloat2 = np.array([3-2j, 1+8j, 2+4j], dtype = np.complex64)
print(arr_cfloat1.dtype)
print(arr_cfloat2.dtype, '\n')

#Unsigned Integer (Doesn't store negative numbers)
arr_uint1 = np.array([255,66,4,12,3], dtype = np.uint8)
#arr_uint1 = np.array([255,-66,4,12,3], dtype = np.uint8) Error: Negative sign
print(arr_uint1, '\n')

#Converting Data Type on Existing Arrays => astype()

#Convert from float to interger
arr_float3 = np.array([1.0,2.0,3.0,4.0,5.0])
new_float3 = arr_float3.astype('i')
print(new_float3)
print(new_float3.dtype)


arr_float4 = np.array([1.0,2.0,3.0,4.0,5.0])
new_float4 = arr_float4.astype(int)
print(new_float4)
print(new_float4.dtype, '\n')

#Convert from float to boolean
arr_float5 = np.array([0.1,1.0,2.0,3.0,4.0,5.0])
new_float5 = arr_float5.astype(bool)
print(new_float5)
print(new_float5.dtype, '\n')

#Convert from integer to boolean
arr_int5 = np.array([0,1,2,3,4,5])
new_int5 = arr_int5.astype(bool)
print(new_int5)
print(new_int5.dtype, '\n')

#Convert from string to int
arr_string7 = np.array(['25', '23', '22']) #Error if the string contains non - integer values
new_string7 = arr_string7.astype(int)
print(new_string7, '\n')

#Convert from complex float to boolean
arr_cfloat3 = np.array([0-0j, 1+0j, 0+4j, 2+3j, 5-7j])
new_cfloat3 = arr_cfloat3.astype(bool)
print(new_cfloat3, '\n')

#Play around the code to convert from one data types to another...