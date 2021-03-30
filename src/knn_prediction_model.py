# VERY SIMPLE PREDICTION MODEL #
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import ml_preprocessor as ml_p

class knn_model:

    # init the object with the preprocessed dataframe and create testing and training sets
    def __init__(self, mlp: ml_p):
        self.mlp = mlp
        self.X_train, self.X_test, self.y_train, self.y_test = self.mlp.getSets()
        self.model = None
        self.score = None

    def createModel(self, neighbors: int = 1):
        # setting up KNN classifier and fitting it to the training data
        #steps = [('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=neighbors))]
        #self.knn = Pipeline(steps)
        self.model = KNeighborsClassifier(n_neighbors=neighbors, n_jobs=-1)
        self.model.fit(self.X_train, self.y_train)
        self.score = self.model.score(self.X_test, self.y_test)

    def predictData(self, data: dict):

        X_new = self.mlp.preprocessInput(data)
        prediction = self.model.predict(X_new)

        return prediction, self.score