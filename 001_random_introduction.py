from numpy import random
print('a random integer from 0 - 50')
r = random.randint(50)
print(r)

print('\nall integers from 0 - 100 in the range 0 - 50')
for i in range(100):
    r = random.randint(50)
    print(r)

print('\n1-D array containing random integers')
r = random.randint(50, size = 10)
print(r)

print('\n2-D array containing random integers')
r = random.randint(50, size = (5, 10)) # random integers in the range 0 - 50 containing 5 rows and 10 columns
print(r)

print('\n3-D array containing random integers')
r = random.randint(50, size = (3, 5, 10)) # random integers in the range 0 - 50 containing 3 depths, 5 rows and 10 columns
print(r)

print('\nFloats => rand() => a random floating number between 0 and 1')
r = random.rand() 
print(r)

print('\n1-D array containing random floating numbers')
r = random.rand(5) 
print(r)

print('\n2-D array containing random floating numbers')
r = random.rand(5, 8) # random floating numbers containing 5 rows and 8 columns
print(r)

print('\n3-D array containing random floating numbers')
r = random.rand(2, 5, 8) # random floating numbers containing 2 depths, 5 rows and 8 columns
print(r)

print('\nGenerate a random number from an array => choice()')
r = random.choice([2,5,8,10])
print(r)

print('\n1-D array that contain values in the array')
r = random.choice([2,5,8,10], size = 10)
print(r)

print('\n2-D array that contain values in the array')
r = random.choice([2.1,5.5,8.6,10.8], size = (2,4))
print(r)

print('\n3-D array that contain values in the array')
r = random.choice([2,5,8,10], size = (3,4,5))
print(r)