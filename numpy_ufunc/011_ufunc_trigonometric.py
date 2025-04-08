import numpy as np
print('Trigonometric Functions')
x = np.sin(np.pi/6) # sin (30) => pi/6 in radians
y = np.cos(np.pi/6) # cos (30) => pi/6 in radians
z = np.tan(np.pi/6) # tan (30) => pi/6 in radians
print(x)
print(y)
print(z)

print('\nTrigonometric Functions => In Array')
arr = np.array([np.pi, np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6])
result1 = np.sin(arr)
result2 = np.cos(arr)
result3 = np.tan(arr)
print(result1)
print(result2)
print(result3)

print('\nConvert Degrees Into Radians')
x = np.deg2rad(90)
arr = np.array([30, 45, 60, 90, 120, 150, 180, 270, 360])
result = np.deg2rad(arr)
print(x)
print(result)

print('\nConvert Radians Into Degrees')
x = np.rad2deg(np.pi/2)
arr1 = np.array([np.pi, np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6])
arr2 = np.array([2*np.pi, 2*np.pi/2, 4*np.pi/3, 2*np.pi/4, 7*np.pi/5, 3*np.pi/6])
print(np.rad2deg(arr1))
print(np.rad2deg(arr2))

print('\nFinding Angles')
x = np.arcsin(0.5)
y = np.arccos(0.5)
z = np.arctan(1)
print(x)
print(np.rad2deg(x)) # convert from radian to degree
print(y)
print(np.rad2deg(y))
print(z)
print(np.rad2deg(z))

print('\nAngles of Each Value in Arrays')
arr = np.array([0.5, 1, -1, 0.8665])
result1 = np.arcsin(arr)
result2 = np.arccos(arr)
result3 = np.arctan(arr)
print(result1)
print(result2)
print(result3)

print('\nHypotenuse')
opposite = 3
adjacent = 4
result = np.hypot(opposite, adjacent)
print(result)
