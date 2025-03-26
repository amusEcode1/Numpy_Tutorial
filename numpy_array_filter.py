import numpy as np
print('Filtering Arrays')
arr = np.array([1,3,7,10,20,25,60])
filter_arr = [False, False, False, True, False, True, True] # Exclude the value at index False from the filtered array
print(arr[filter_arr])

print('\n Filter array without loop')
arr = np.array([0,5,10,15,20,25,30,35,40,45,50])
filter_arr = arr > 35
print(arr[filter_arr])
print(filter_arr)

print('\nFilter Array in form of loop')
arr = np.array([0,5,10,15,20,25,30,35,40,45,50])
filter_arr = []
for numbers in arr:
    if numbers > 35 or numbers < 10:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
print(arr[filter_arr])
print(filter_arr)

print('\nArray that stores odd numbers in the filtered without using loop')
arr = np.array([0,1,2,3,4,6,8,9,10,13,15,17,20])
filter_arr = arr % 2 == 1
print(arr[filter_arr])
print(filter_arr)

print('\nArray that stores odd numbers in the filtered array using loop')
arr = np.array([0,1,2,3,4,6,8,9,10,13,15,17,20])
filter_arr = []
for numbers in arr:
    if numbers % 2 == 1:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
print(arr[filter_arr])
print(filter_arr)