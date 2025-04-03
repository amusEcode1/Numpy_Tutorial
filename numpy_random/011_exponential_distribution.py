from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Exponential Distribution')
x = random.exponential(size = 50)
y = random.exponential(scale = 1, size = (2,3))
print(x)
print(y)

print('\nVisualization of Exponential Distribution')
sns.displot(random.exponential(size = 1000), kind = 'kde')
plt.show()

print('\nDifference between Poisson and Exponential Distribution')
data = {
    'poisson': random.poisson(lam = 6, size = 100),
    'exponential': random.exponential(size = 200)
}
sns.displot(data, kind = 'kde')
plt.show()



