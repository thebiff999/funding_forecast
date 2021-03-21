import pandas as pd
import category_difference as cd
import duration
import goal_variable as gv
import importer
import name_length as nl
import Removing_NaN_in_names as rm_names
import percentage_reached_column as percentage

class preprocessor:

    def __init__(self, source: str = "ks-projects-201801.csv"):
        self.source = source
        self.dataframe = importer.load_file(source)

    def setSource(self, source: str):
        self.source = source

    def cleanDataset(self, source: str = "") -> pd.DataFrame:

        #check if the source parameter is filled or the object has been initialized with a source
        if (source == ""):
            source = self.source
        if (source == ""):
            print("missing source")

        #load the file and clean the data
        df = importer.load_file(source)
        df = gv.clean_state_column(df)
        df = rm_names.remove_nan_names(df)

        #add additional columns
        df = duration.add_column(df)
        df = nl.add_column(df)
        df = cd.add_column(df)
        df = percentage.add_column(df)

        self.dataframe = df
        return df

    def getDataset(self) -> pd.DataFrame:
        return self.dataframe

    def exportDataset(self):
        self.dataframe.to_csv("kickstarter.csv")