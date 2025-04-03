from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Logistic Distribution')
x = random.logistic(loc = 2, scale = 5, size = 20)
y = random.logistic(loc = 1, scale = 2, size = (3,7))
print(x)
print(y)

print('Visualization of Logistic Distribution')
sns.displot(random.logistic(size = 10), kind = 'kde')
plt.show()

print('\nDifference between Normal and Logistic Distribution')
data = {
    'normal': random.normal(loc = 4, scale = 9, size = 2000),
    'logistic': random.logistic(size = 1000)
}
sns.displot(data, kind = 'kde')
plt.title('Normal Distribution vs Logistic Distribution')
plt.show()

print('\nDifference between Poisson and Logistic Distribution')
data = {
    'poisson': random.poisson(lam = 6, size = 2000),
    'logistic': random.logistic(size = 1000)
}
sns.displot(data, kind = 'kde')
plt.title('Poisson Distribution vs Logistic Distribution')
plt.show()
