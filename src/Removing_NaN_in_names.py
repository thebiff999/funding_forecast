#Welche Daten fehlen ?                                                                                               
                                                                                                                     
#print(df.isnull().sum())                            #name has 4 missing values                                       
#print(df[df.name.isnull()])                         #every row where name is NaN                                     
#print(df.shape)                                     #shape of the df                                                 
#df = df.dropna(subset=['name'])                     #dropping                                                        
#print(df.shape)                                     #shape of df with NaN values removed (4 less thah in rows)  
#print(df[df.name.isnull()])                         #empty data frame for missing values in name (successful removal)
#print(df.head(5))                                   #df is the new dataframe without missing values                                                              

import pandas as pd

def remove_nan_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset = ['name'])

    try:
        assert(df.name.isna().sum() == 0)
    except AssertionError as e:
        print("The removal of NaN values in the names colmn has failed")
        print(e)

    return df