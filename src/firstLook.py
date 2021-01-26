import pandas as pd
from pathlib import Path

#resolve path to csv file from anywhere
filename = "ks-projects-201801.csv"
path = Path(__file__).resolve().parents[1]
file = Path(path, filename)

df = pd.read_csv(file)
print(df.describe())