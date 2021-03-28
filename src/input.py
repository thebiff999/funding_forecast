import pandas as pd
import ml_preprocessor as mlp

# take input from user
name = input('Please enter your project name: ')
duration = int(input('Please enter the duration of your project in days: '))
main_category = input('Please enter the main category of your project: ')
category = input('Please enter the sub category of your project: ')
country = input('Please enter your two-character country-code: ')
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

df = pd.DataFrame(data, index=[0])
df = mlp.preprocessInput(df)
print(df)
print('The success probability of your project is ...')