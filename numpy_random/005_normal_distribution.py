from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Normal Distribution')
x = random.normal(size = (10))
print(x)

print('\nNormal Distribution Mean (Loc), Standard Deviation (Scale)')
x = random.normal(loc = 2, scale = 3, size = (3,5))
print(x)

print('Visualization of Normal Distribution')
sns.displot(random.normal(size = (3,6)))
sns.displot(random.normal(size = 100), kind = 'kde')
sns.displot(random.randn(100,200), kind = 'kde')
plt.show()