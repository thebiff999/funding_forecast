import importer
import duration
import goal_variable
import percentage_reached_column as percentage
import Removing_NaN_in_names as rm_names

#load the file and clean the data
df = importer.load_file()
df = goal_variable.clean_state_column(df)
df = rm_names.remove_nan_names(df)

#add additional columns
df = duration.add_column(df)
df = percentage.add_column(df)
df = percentage.add_column(df)
print(df.info())