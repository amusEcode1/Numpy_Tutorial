from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Pareto Distribution')
x = random.pareto(a = 2, size = 20)
y = random.pareto(a = 5, size = (3,6))
print(x)
print(y)

print('\nVisualization of Pareto Distribution')
sns.displot(random.pareto(a = 2, size = (3,6)), kind = 'kde')
plt.show()

print('\nDifference between Rayleigh and Pareto Distribution')
data = {
    'Rayleigh': random.rayleigh(scale = 3, size = 1000),
    'Pareto': random.pareto(a = 2, size = 200),
}
sns.displot(data, kind = 'kde')
plt.show()