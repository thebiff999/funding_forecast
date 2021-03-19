import matplotlib.pyplot as plt
import seaborn as sns

#Name length distribution for states

plt.subplot(1,2,1)
plt.title('Name length and project state')
sns.boxplot( x=df["state"],
                y=df['name_length'])
plt.xlabel('State')
plt.ylabel('Number of Characters')

plt.subplot(1,2,2)
sns.violinplot( x=df["state"],
                y=df['name_length'])
plt.xlabel('State')
plt.ylabel('Number of Characters')
plt.show()

#There is not much of a difference in name length
#most of the names of successful projects seem to be a little bit longer than their counterparts