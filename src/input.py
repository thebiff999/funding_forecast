import knn_prediction_model as knn
import svm_prediction_model as svm
import preprocessor as pre

#init a preprocessor object to extract dataframe column values to print possible inputs
print('preparing the dataframe')
p = pre.preprocessor()
p.cleanDataset()
df = p.getDataset()

#create the knn model
#print('creating the knn model')
#model = knn.knn_model()
#model.createModel(2)

#create the svm model
print('creating the svm model')
model = svm.svm_model()
model.createModel()

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

    model.predictData(data)