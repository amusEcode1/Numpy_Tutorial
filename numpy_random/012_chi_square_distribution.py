from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
print('Chi Square Distribution')
x = random.chisquare(df = 2, size = 1000)
y = random.chisquare(df = 5, size = (3,7))
print(x)
print(y)

print('\nVisualization of Chi Square Distribution')
sns.displot(random.chisquare(df = 1, size = 1000), kind = 'kde')
plt.show()