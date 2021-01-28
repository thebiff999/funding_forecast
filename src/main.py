import importer
import duration

df = importer.load_file()
df = duration.add_duration(df)
print(df.head)