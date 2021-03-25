import pandas as pd
import numpy as np

#read the csv
df = pd.read_csv('kickstarter.csv')

#drop unnecessary columns
df = df.drop(columns=['ID', 'name', 'deadline', 'launched', 'pledged', 'backers', 'usd pledged', 'usd_pledged_real', 'percentage_reached_real', 'duration'])

#remap values to 1 and 0
dict1 = {'successful': 1, 'failed': 0}
df['state'] = df['state'].map(dict1)
dict2 = {True : 1, False : 0}
df['category_difference'] = df['category_difference'].map(dict2)

#create dummy columns
dummy_main_category = pd.get_dummies(df['main_category'])
dummy_category = pd.get_dummies(df['category'])
dummy_currency = pd.get_dummies(df['currency'])
dummy_country = pd.get_dummies(df['country'])

#drop dummy source columns
df = df.drop(columns=['main_category', 'category', 'currency', 'country'])

#concat dataframe and dummy columns
df_normalized = pd.concat([df, dummy_main_category, dummy_category, dummy_currency, dummy_country], axis=1)

print(df_normalized.head())