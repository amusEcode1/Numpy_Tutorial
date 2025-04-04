from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Rayleigh Distribution => For Signal Processing')
x = random.rayleigh(scale = 3, size = 20)
y = random.rayleigh(scale = 3, size = (3,6))
print(x)
print(y)

print('\nVisualization of Rayleigh Distribution')
sns.displot(random.rayleigh(scale = 2, size = (3,6)), kind = 'kde')
plt.show()

print('\nDifference between Chi Square and Rayleigh Distribution')
data = {
    'chi square': random.chisquare(df= 4, size = 200),
    'Rayleigh': random.rayleigh(scale = 3, size = 1000)
}
sns.displot(data, kind = 'kde')
plt.show()