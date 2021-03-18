import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Boxplots State vs. Goal (Real US$)
plt.subplot(1,2,1)
sns.boxplot(x=df["state"],
            y=df["usd_goal_real"])
plt.ylabel('Goal (Real US$)')
plt.ylim(-5000, 50000)
plt.xlim(None, None)

#Violinplots State vs. Goal (Real US$)
plt.subplot(1,2,2)
sns.violinplot(x=df["state"],
                y=df["usd_goal_real"])
plt.ylabel('Goal (US$)')
plt.ylim(-5000, 100000)
plt.xlim(None, None)
plt.show()


df_failed = df[df['state'].isin(['failed'])]
print('Maximum of real goal failed projects')
print(df_failed['usd_goal_real'].max())
print('Minimum of real goal failed projects')
print(df_failed['usd_goal_real'].min())
print('Median of real goal failed projects')
print(np.median(df_failed['usd_goal_real']))

df_successful = df[df['state'].isin(['successful'])]
print(df_successful['state'].unique())
print('Maximum of  goal successful projects')
print(df_successful['usd_goal_real'].max())
print('Minimum of goal successful projects')
print(df_successful['usd_goal_real'].min())
print('Median of real goal failed projects')
print(np.median(df_successful['usd_goal_real']))

#Maximum and Median of real goal is much larger for failed Projects
