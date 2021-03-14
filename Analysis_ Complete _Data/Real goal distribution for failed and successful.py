import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.subplot(1,2,1)
sns.boxplot(x=df["state"],
            y=df["usd_goal_real"])
plt.ylabel('Goal (US$)')

plt.subplot(1,2,2)
sns.violinplot(x=df["state"],
                y=df["usd_goal_real"])
plt.ylabel('Goal (US$)')
plt.show()


print(df['state'].unique())

dffailed = df[df['state'].isin(['failed'])]
print('Maximum of real goal failed projects')
print(dffailed['usd_goal_real'].max())
print('Minimum of real goal failed projects')
print(dffailed['usd_goal_real'].min())
print('Median of real goal failed projects')
print(np.median(dffailed['usd_goal_real']))

dfsuccessful = df[df['state'].isin(['successful'])]
print(dfsuccessful['state'].unique())
print('Maximum of  goal successful projects')
print(dfsuccessful['usd_goal_real'].max())
print('Minimum of goal successful projects')
print(dfsuccessful['usd_goal_real'].min())
print('Median of real goal failed projects')
print(np.median(dfsuccessful['usd_goal_real']))


#Maximum and Median of real goal is much larger for failed Projects
