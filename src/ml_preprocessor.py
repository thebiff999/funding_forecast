import pandas as pd
import numpy as np
import preprocessor as p

# prepare the user input in the same way as the training data to use it for prediction
def preprocessInput(dataframe: pd.DataFrame) -> pd.DataFrame:
    df = dataframe
    df = createDummies(df)
    return df

# method to prepate the dataframe for machine learning
# uses the default csv file, calls preprocessor.py
def getDataFrame() -> pd.DataFrame:
    #load the csv from preprocessor.py
    preprocessor = p.preprocessor("ks-projects-201801.csv")
    df = preprocessor.cleanDataset()
    preprocessor.exportDataset()
    df = main(df)
    return df

# method to prepate the dataframe for machine learning
# does not use the default file, a dataframe has to be given as argument
def preprocess(dataframe: pd.DataFrame) -> pd.DataFrame:
    df = dataframe
    df = main(df)
    return df    

def main(dataframe: pd.DataFrame) -> pd.DataFrame:
    df = dataframe

    #drop unnecessary columns
    df = df.drop(columns=['ID', 'name', 'deadline', 'launched', 'pledged', 'backers', 'usd pledged', 'usd_pledged_real', 'percentage_reached_real'])

    #remap values to 1 and 0
    dict1 = {'successful': 1, 'failed': 0}
    df['state'] = df['state'].map(dict1)
    dict2 = {True : 1, False : 0}
    df['category_difference'] = df['category_difference'].map(dict2)
    df_normalized = createDummies(df)

    return df_normalized

def createDummies(dataframe: pd.DataFrame) -> pd.DataFrame:
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