import pandas as pd

def clean_country_column(df: pd.DataFrame) -> pd.DataFrame:
    mask = df['country'] != 'N,0"'
    df = df[mask]
    #df.drop(df[df.country == 'N,0"'].index, inplace=True)

    try:
        assert(df[df.country=='N,0"'].empty)
        print(df[df.country=='N,0"'])
    except AssertionError as e:
        print("Removing NaN countries has failed")
        print(e)

    return df