from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Poisson Distribution')
x = random.poisson(lam = 6, size = 10)
print(x)

print('\nVisualization of Poisson Distribution')
sns.displot(random.poisson(lam = 4, size = 20))
plt.title('Poisson Distribution')
plt.show()

print('\nDifference between Normal and Poisson Distribution')
data = {
    'normal': random.normal(loc = 4, scale = 9, size = 150),
    'poisson': random.poisson(lam = 5, size = 300)
}
sns.displot(data, kind = 'kde')
plt.title('Normal Distribution vs Poisson Distribution')
plt.show()

print('\nDifference between Binomial and Poisson Distribution')
data = {
    'binomial': random.binomial(n = 10, p = 0.8, size = 600),
    'poisson': random.poisson(lam = 9, size = 800)
}
sns.displot(data, kind = 'kde')
plt.title('Binomial Distribution vs Poisson Distribution')
plt.show()
