from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Ziph Distribution')
x = random.zipf(a = 2, size = 20)
y = random.zipf(a = 5, size = (3,6))
print(x)
print(y)

print('\nVisualization of Pareto Distribution')
x = random.zipf(a = 2, size = 1000)
sns.displot(x[x < 10])
sns.displot(x[x < 10], kind = 'kde')
plt.show()