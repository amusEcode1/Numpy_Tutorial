import numpy as np
#NumPy Array Copy vs View

print('COPY') #changes made to the array doesn't affect the copy(since it owns the data)
arr1 = np.array([5,6,7,8,9])
copy_arr = arr1.copy() #exact position to place the copy() if you want to copy the original array.
arr1[2] = 2 #copy() placed after this line, copies the modified array.
print(arr1)
print(copy_arr, '\n')

print('VIEW') #changes made to the array, affects the view(since it doesn't own the data)
arr2 = np.array([5,6,7,8,9])
view_arr = arr2.view() #view() can be placed at any position.
arr2[1] = 5
print(arr2)
print(view_arr, '\n')

print('Check if the Array Owns its Data') #using the BASE attribute, returns None if the address owns the data(COPY)
arr3 = np.array([5,6,7,8,9])
copy_base = arr3.copy()
view_base = arr3.view()
print(copy_base.base)
print(view_base.base)

#Play around the code using other datatypes...