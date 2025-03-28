from numpy import random
print('Random Distribution for 1-D array')
r = random.choice([2,3,6,7,8], p = [0,0.2,0,0.5,0.3], size = (10))
'''2 and 6 has 0% chance(It will never be selected)
3 has 20% chance of being choosen
7 has 50% chance of being choosen
8 has 30% chance of being choosen
The sum of all the probability numbers should be 1
'''
print(r)

print('\nRandom Distribution for 2-D array')
r = random.choice([2,3,6,7,8], p = [0,0.2,0.1,0.3,0.4], size = (5,8))
print(r)

print('\nRandom Distribution for 3-D array')
r = random.choice([2,3,6,7,8], p = [0,0,0,1.0,0], size = (3,5,8)) #7 will be selected 100%
print(r)