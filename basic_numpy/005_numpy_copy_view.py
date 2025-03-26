import numpy as np
#NumPy Array Copy vs View

print('COPY') #changes made to the array doesn't affect the copy(since it owns the data)
arr = np.array([5,6,7,8,9])
arr_copy = arr.copy() #exact position to place the copy() if you want to copy the original array.
arr[2] = 2 #copy() placed after this line, copies the modified array.
print(arr)
print(arr_copy, '\n')

print('VIEW') #changes made to the array, affects the view(since it doesn't own the data) and vice versa
arr = np.array([5,6,7,8,9])
arr_view = arr.view() #view() can be placed at any position.
arr[1] = 5
print(arr)
print(arr_view, '\n')

print('Check if the Array Owns its Data') #using the BASE attribute, returns None if the address owns the data(COPY)
arr = np.array([5,6,7,8,9])
arr_copy = arr.copy()
arr_view = arr.view()
print(arr_copy.base)
print(arr_view.base)

#Play around the code using other datatypes...
