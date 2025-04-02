from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Uniform Distribution')
x = random.uniform(size = (5,8))
print(x)

print('\nVisualization of Uniform Distribution')
sns.displot(random.uniform(size = 2000), kind = 'kde')
plt.title('Visualization of Uniform Distribution')
plt.show()

print('\nDifference between Normal and Uniform Distribution')
data = {
    'normal': random.normal(loc = 4, scale = 9, size = 2000),
    'poisson': random.uniform(size = 1000)
}
sns.displot(data, kind = 'kde')
plt.title('Normal Distribution vs Uniform Distribution')
plt.show()