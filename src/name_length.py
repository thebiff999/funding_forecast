def add_column(df):

    df["name_length"] = df["name"].astype("str").map(len)

    try:
        (df["name_length"].isna().sum())
    except AssertionError as e:
        print("Adding the name_length column has failed")
        print(e)