from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.multinomial(n = 4, pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
y = random.multinomial(n = 4, pvals = [0.1, 0.2, 0.7], size = (2,5))
print(x)
print(y)

print('\nSimulating 1000 survey responses')
responses = random.multinomial(n = 1000, pvals = [0.6, 0.3, 0.1])
print('Survey Responses:')
print(f'Yes: {responses[0]}')
print(f'No: {responses[1]}')
print(f'Maybe: {responses[2]}')