# VERY SIMPLE PREDICTION MODEL #
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import ml_preprocessor as mlp

class knn_model:

    # init the object with the preprocessed dataframe and create testing and training sets
    def __init__(self):
        # get prepared dataframe from the machine learning preprocessor script
        self.ml_p = mlp.ml_preprocessor()
        self.df = self.ml_p.getDataFrame()

        # create array with target values
        self.kickstarter_dataset_target = self.df['state'].values

        # remove the target values from the dataframe
        self.df = self.df.drop(['state'], axis=1)

        # create array with data
        self.kickstarter_dataset_data = self.df.values

        # create testing and training sets (25% test)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.kickstarter_dataset_data,
                                                            self.kickstarter_dataset_target,
                                                            test_size=0.25,
                                                            random_state=0)
        self.knn = None

    def createModel(self, neighbors: int = 1):
        # setting up KNN classifier and fitting it to the training data
        self.knn = KNeighborsClassifier(neighbors)
        # n_neighbours = 1 is probably not optimal an will need to be adjusted
        self.knn.fit(self.X_train, self.y_train)

    def predictData(self, data: dict):
        # insert the values of your project you want o make a prediction for

        X_new = self.ml_p.preprocessInput(data)

        prediction = self.knn.predict(X_new)
        kickstarter_dataset_target_names = np.array(['failed', 'successful'])

        if (prediction == 1):
            print("Your campaign has a high probability of success")
        elif (prediction == 0):
            print("Your campaign has a low chance of success. It's likely to fail.")
