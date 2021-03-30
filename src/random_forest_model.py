# VERY SIMPLE PREDICTION MODEL #
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import ml_preprocessor as ml_p

class rf_model:

    # init the object with the preprocessed dataframe and create testing and training sets
    def __init__(self, mlp: ml_p):
        self.mlp = mlp
        self.X_train, self.X_test, self.y_train, self.y_test = self.mlp.getSets()
        self.model = None
        self.score = None

    def createModel(self):
        # setting up SVM classifier and fitting it to the training data
        steps = ([('scaler', StandardScaler()),('model', RandomForestClassifier(n_estimators=100, min_samples_leaf=5, random_state=42, n_jobs=-1))])
        self.model = Pipeline(steps)
        self.model.fit(self.X_train, self.y_train)
        self.score = self.model.score(self.X_test, self.y_test)

    def predictData(self, data: dict):

        X_new = self.mlp.preprocessInput(data)
        prediction = self.model.predict(X_new)

        return prediction, self.score