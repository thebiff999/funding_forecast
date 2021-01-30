def add_column(df):

    difference = df["main_category"] == df["category"]
    df["category_difference"] = difference

    try:
        assert df["category_difference"].isna().sum() == 0
    except AssertionError as e:
        print("Adding the category_difference column has failed")
        print(e)

    return df
