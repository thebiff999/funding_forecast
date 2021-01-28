import pandas as pd
import datetime as dt

def add_duration(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("add_duration has to be called with a DataFrame as parameter")
    elif df['launched'].empty:
        raise ValueError("The DataFrame does not have the correct columns")
    else:
        return process(df)

def process(df):
    #convert string to timestamp to date for the 'launched' column
    df['launched'] = pd.to_datetime(df['launched'])
    df['launched'] = df['launched'].dt.date

    #convert string to date for the 'deadline' column
    df['deadline'] = pd.to_datetime(df['deadline'])
    df['deadline'] = df['deadline'].dt.date

    #check if conversions were successful
    assert df['launched'].isna().sum() == 0
    assert df['deadline'].isna().sum() == 0

    #create duration and assert completeness
    df['duration'] = df['deadline'] - df['launched']
    assert df['duration'].isna().sum() == 0

    return df