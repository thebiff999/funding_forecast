import matplotlib.pyplot as plt

percentage_reached_real = df['percentage_reached_real']
duration_days = df['duration_days']

plt.scatter(duration_days, percentage_reached_real)
plt.xlabel('Duration (in days)')
plt.ylabel('Percentage of the Goal reached')
plt.show()