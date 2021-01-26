import pandas as pd
path = "../"
filename = "ks-projects-201801.csv"
csv_file = path + filename
df = pd.read_csv(csv_file)
print(df.head())