import pandas as pd

def clean_name_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset = ['name'])

    try:
        assert(df.name.isna().sum() == 0)
    except AssertionError as e:
        print("The removal of NaN values in the names colmn has failed")
        print(e)

    return df
