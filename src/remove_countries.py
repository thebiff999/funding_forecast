import pandas as pd

def clean_country_column(df: pd.DataFrame) -> pd.DataFrame:
    df.drop(df[df.country == 'N,0"'].index, inplace=True)

    try:
        assert(df[df.country=='N,0"'].empty)
    except AssertionError as e:
        print("Removing NaN countries has failed")
        print(e)

    return df