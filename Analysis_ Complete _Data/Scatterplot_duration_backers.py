import matplotlib.pyplot as plt

duration_float = df['duration_days']
backers = df['backers']

plt.scatter(duration_float,backers)
plt.xlabel('Duration (in days)')
plt.ylabel('Backers')
plt.show()

#No real Realtionship can be found between The funding duration and the total number of backers
