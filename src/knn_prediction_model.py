# VERY SIMPLE PREDICTION MODEL #
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# make new column with numerical codes for state
df['code'] = pd.factorize(df['state'])[0]
# code 0 -> state = failed
# code 1 -> state = successful

# Drop unnecessary columns #
df = df.drop(['ID', 'country', 'main_category', 'category', 'currency', 'name', 'deadline', 'launched', 'pledged',
              'backers', 'usd pledged', 'usd_pledged_real', 'usd_goal_real', 'category_difference', 'duration',
              'percentage_reached_real', 'state'],
             axis=1)

kickstarter_dataset_target = df['code'].values                          # create array with target values

print(kickstarter_dataset_target)                                       # glance at data
print('Type of target:{}'.format(type(kickstarter_dataset_target)))     # make sure the format is right
print('Shape of target:{}'.format(kickstarter_dataset_target.shape))

df = df.drop(['code'], axis=1)                                           # remove the code from df

kickstarter_dataset_data = df.values                                    # create array with data

print(kickstarter_dataset_data)                                         # glance at data
print('Type of data:{}'.format(type(kickstarter_dataset_data)))         # make sure the format is right
print('Shape of data:{}'.format(kickstarter_dataset_data.shape))



# create testing and training sets (25% test)
X_train, X_test, y_train, y_test = train_test_split(kickstarter_dataset_data,
                                                    kickstarter_dataset_target,
                                                    test_size=0.25,
                                                    random_state=0)


# setting up KNN classifier and fitting it to the training data
knn = KNeighborsClassifier(n_neighbors=1)
# n_neighbours = 1 is probably not optimal an will need to be adjusted
knn.fit(X_train, y_train)

# setting up predictions
# insert the values of your project you want o make a prediction for
# we just use made up numbers for demonstration
goal = 20000
duration_days = 30
name_length = 20

X_new = np.array([[goal, duration_days, name_length]])

prediction = knn.predict(X_new)
kickstarter_dataset_target_names = np.array(['failed', 'successful'])

print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(kickstarter_dataset_target_names[prediction]))