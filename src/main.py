import importer
import duration
import goal_variable

df = importer.load_file()
df = duration.add_duration(df)
df = goal_variable.clean_state_column(df)
print(df.info())