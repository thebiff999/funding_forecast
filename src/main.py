import preprocessor as p

preprocessor = p.preprocessor("ks-projects-201801.csv")
df = preprocessor.cleanDataset()
print(df.info())