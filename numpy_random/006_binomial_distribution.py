from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Binomial Distribution')
x = random.binomial(n = 10, p = 0.0, size = 10) #since p=0, there is a no chance of success (e.g., probability of getting heads in a coin toss)
y = random.binomial(n = 20, p = 0.2, size = 10) #since p=0.8, there is a 80% chance of success
z = random.binomial(n = 20, p = 0.8, size = (2,4))
print(x)
print(y)
print(z)

print('\nVisualization of Binomial Distribution')
sns.displot(random.binomial(n = 15, p = 0.8, size = 1000))
plt.show()

print('\nDifference between Normal and Binomial Distribution')
data = {
    'normal': random.normal(loc = 10, scale = 4, size = 200),
    'binomial': random.binomial(n = 20, p = 0.6, size = 400)
}
sns.displot(data, kind = 'kde')
plt.show()