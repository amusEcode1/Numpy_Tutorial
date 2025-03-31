import matplotlib.pyplot as plt
import seaborn as sns 
print('Plotting a Displot')
sns.displot([0,1,2,3,4,5,6,7,8,9])
plt.show()

print('\nPlotting a Displot Without the Histogram')
sns.displot([0,1,2,3,4,5,6,7,8,9], kind = 'kde')
plt.show()

print('\nPlotting a Displot Using a Histogram with KDE overlay')
sns.displot([0,1,2,3,4,5,6,7,8,9], kde = True)
plt.show()