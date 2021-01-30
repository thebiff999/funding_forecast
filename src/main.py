import pandas as pd
import importer
import goal_variable
import Removing_NaN_in_names as rm_names
import duration
import name_length
import category_difference as difference
import percentage_reached_column as percentage

#load the file and clean the data
df: pd.DataFrame
df = importer.load_file()
df = goal_variable.clean_state_column(df)
df = rm_names.remove_nan_names(df)

#add additional columns
df = duration.add_column(df)
df = name_length.add_column(df)
df = difference.add_column(df)
df = percentage.add_column(df)
print(df.info())