import preprocessor as p
pre = p.preprocessor()

df = pre.cleanDataset()
print(df['state'])