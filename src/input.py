import ml_preprocessor as ml_p
import knn_prediction_model as knn
import svm_prediction_model as svm
import random_forest_model as rfm
import preprocessor as pre
from time import time
import pandas as pd

def load_dataframe():
    try:
        df = pd.read_csv('kickstarter.csv')
    except:
        print("kickstarter.csv not found, loading a new dataframe")
        p = pre.preprocessor()
        p.cleanDataset()
        df = p.getDataset()
    finally:
        return df

#create the knn model
def use_knn_model(mlp: ml_p):
    print('creating the nearest neighbors model')
    model = knn.knn_model(mlp)
    model.createModel(2)
    return model

#create the svm model
def use_svm_model(mlp: ml_p):
    print('creating the support vector machine model')
    model = svm.svm_model(mlp)
    model.createModel()
    return model

#create the rfm model
def use_rf_model(mlp: ml_p):
    print('creating the random forest model')
    model = rfm.rf_model(mlp)
    model.createModel()
    return model

def process_input(df: pd.DataFrame, mlp: ml_p):

    #let the user decide which model he wants to use
    choice = input('Which model do you want to use, SVM [S], nearest neighbor [N], or RandomForest[R] ?')
    if (choice == "S"):
        model = use_svm_model(mlp)
    elif (choice == "N"):
        model = use_knn_model(mlp)
    elif (choice == "R"):
        model = use_rf_model(mlp)
    else:
        print('Invalid input, please repeat')
        input()

    while True:

        # take input from user
        name = input('Please enter your project name: ')

        duration = int(input('Please enter the duration of your project in days: '))

        print('These are the available main categories')
        print(list(set(df['main_category'].values)))
        main_category = input('Please enter the main category of your project: ')

        print('These are the available sub categories')
        print(list(set(df['category'].values)))
        category = input('Please enter the sub category of your project: ')

        country = input('Please enter your two-character country-code: ')

        print('These are the available currencies')
        print(list(set(df['currency'].values)))
        currency = input('Please enter the funding three-character currency: ')

        goal = int(input('Please enter your project goal in USD: '))

        # process user input
        name_length = len(name)
        if (main_category == category):
            category_difference = 0
        else:
            category_difference = 1

        data = {
            'category': category,
            'main_category': main_category,
            'currency': currency,
            'country': country,
            'usd_goal_real': goal,
            'duration_days': duration,
            'name_length': name_length,
            'category_difference': category_difference
        }
        start = time()
        prediction, score = model.predictData(data)
        end = time()
        duration = end - start
        if (prediction == 1):
            print("Your campaign has a high probability of success")
        elif (prediction == 0):
            print("Your campaign has a low chance of success. It's likely to fail.")
        print("The accuracy of this prediction is " + str(score) + "%")
        print("Time taken: " + str(duration))

df = load_dataframe()
mlp = ml_p.ml_preprocessor(dataframe=df)
process_input(df, mlp)