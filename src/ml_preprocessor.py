import pandas as pd
import numpy as np
import preprocessor as p
from sklearn.model_selection import train_test_split

class ml_preprocessor:

    def __init__(self, path="ks-projects-201801.csv", dataframe: pd.DataFrame=None):

        if (dataframe.empty):
            preprocessor = p.preprocessor(path)
            self.dataframe = preprocessor.cleanDataset()
        else:
            self.dataframe = dataframe

        self.template = self.dataframe
        self.dataframe = self.main(self.dataframe)
        #print(self.dataframe.head())

    # prepare the user input in the same way as the training data to use it for prediction
    def preprocessInput(self, data: dict):
        # append the input into dataframe and preprocess it like the model data
        df = self.template.append(data, ignore_index = True)
        df = df.drop(columns=['state','ID', 'name', 'deadline', 'launched', 'pledged', 'backers', 'usd pledged', 'usd_pledged_real', 'percentage_reached_real', 'goal'])
        df = self.createDummies(df)

        # cut out the input row and format it to a 2-D numpy array
        df = df.iloc[-1,:]
        array = df.to_numpy()
        result = np.array([array])
        return result

    # method to prepate the dataframe for machine learning
    # uses the default csv file, calls preprocessor.py
    def getDataFrame(self) -> pd.DataFrame:
        return self.dataframe

    # method to prepate the dataframe for machine learning
    # does not use the default file, a dataframe has to be given as argument
    def preprocessDataFrame(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        df = dataframe
        df = self.main(df)
        return df    

    # internal method used for dropping and remapping columns, calls the createDummies method
    def main(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        df = dataframe

        #drop unnecessary columns
        df = df.drop(columns=['ID', 'name', 'deadline', 'launched', 'pledged', 'backers', 'usd pledged', 'usd_pledged_real', 'percentage_reached_real', 'goal'])

        #remap values to 1 and 0
        dict1 = {'successful': 1, 'failed': 0}
        df['state'] = df['state'].map(dict1)
        dict2 = {True : 1, False : 0}
        df['category_difference'] = df['category_difference'].map(dict2)
        df_normalized = self.createDummies(df)

        return df_normalized

    #internal method used to create dummy columns
    def createDummies(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        df = dataframe
        #create dummy columns
        dummy_main_category = pd.get_dummies(df['main_category'])
        dummy_category = pd.get_dummies(df['category'])
        dummy_currency = pd.get_dummies(df['currency'])
        dummy_country = pd.get_dummies(df['country'])

        #drop dummy source columns
        df = df.drop(columns=['main_category', 'category', 'currency', 'country'])

        #concat dataframe and dummy columns
        df_normalized = pd.concat([df, dummy_main_category, dummy_category, dummy_currency, dummy_country], axis=1)

        return df_normalized

    def getSets(self):
        kickstarter_dataset_target = self.dataframe['state'].values

        # remove the target values from the dataframe
        df = self.dataframe.drop(['state'], axis=1)

        # create array with data
        kickstarter_dataset_data = df.values

        # create testing and training sets (25% test)
        X_train, X_test, y_train, y_test = train_test_split(kickstarter_dataset_data,
                                                            kickstarter_dataset_target,
                                                            test_size=0.25,
                                                            random_state=0)
        return X_train, X_test, y_train, y_test