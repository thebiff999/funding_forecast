import matplotlib.pyplot as plt
import seaborn as sns

#Barplot and boxplot showing the amount of backers for each main category

plt.subplot(2,1,1)
plt.title('Backers in each main category')
sns.barplot(x=df['main_category'],
               y=df["backers"])
plt.xlabel('Main Category')
plt.ylabel('(Average?) Number of Backers')
plt.ylim(0, 550)

plt.subplot(2,1,2)
sns.boxplot(x=df['main_category'],
            y=df["backers"])
plt.xlabel('Main Category')
plt.ylabel('Number of Backers')
plt.ylim(0, 550)

plt.show()

#games, design, comics and technology seem to be the categories with the highest amount of support