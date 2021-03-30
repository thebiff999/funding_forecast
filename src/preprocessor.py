import pandas as pd
import category_difference as cd
import duration
import goal_variable as gv
import importer
import name_length as nl
import remove_names as rm_names
import percentage_reached_column as percentage
import remove_countries as rm_countries

class preprocessor:

    def __init__(self, source: str = "ks-projects-201801.csv"):
        self.source = source
        self.dataframe = importer.load_file(source)

    def setSource(self, source: str):
        self.source = source

    # cleans and returns the given, or if none is given, the default dataset
    def cleanDataset(self, source: str = "") -> pd.DataFrame:

        #check if the source parameter is filled or the object has been initialized with a source
        if (source == ""):
            source = self.source
        if (source == ""):
            print("missing source")

        #load the file and clean the data
        df = importer.load_file(source)
        df = gv.clean_state_column(df)
        df = rm_names.clean_name_column(df)
        df = rm_countries.clean_country_column(df)

        #add additional columns
        df = duration.add_column(df)
        df = nl.add_column(df)
        df = cd.add_column(df)
        df = percentage.add_column(df)

        self.dataframe = df
        self.exportDataset()
        return df

    def getDataset(self) -> pd.DataFrame:
        return self.dataframe

    def exportDataset(self):
        self.dataframe.to_csv("kickstarter.csv")