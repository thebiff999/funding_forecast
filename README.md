# ms-wt-20-15-FundingForecasteamName
#Projekt zur Ermittlung von Kickstarter-Erfolg

import pandas as pd

##Daten einlesen##
filename = "ks-projects-201801.csv"
df = pd.read_csv(filename, engine='python') # error_bad_lines=False, ,

##Infos##
print(df.info())
print(df.head(5))
print(df['backers'].head(5))
