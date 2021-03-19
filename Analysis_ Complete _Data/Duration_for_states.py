import matplotlib.pyplot as plt
import seaborn as sns

#Funding durastion for states

plt.subplot(1,2,1)
plt.title('Duration and project state')
sns.boxplot( x=df["state"],
             y=df['duration_days'])
plt.xlabel('State')
plt.ylabel('Funding duration (in days)')

plt.subplot(1,2,2)
plt.title('Duration and project state')
sns.violinplot( x=df["state"],
                y=df['duration_days'])
plt.xlabel('State')
plt.ylabel('Funding duration (in days)')
plt.show()

#range of funding duration seems to be larger for failed projects
#still data distribution seems to be very similar for both states
#most projects are open for funding on kickstarter for a month