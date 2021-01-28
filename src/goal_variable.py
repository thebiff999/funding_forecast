#drop rows with values other than failed and successful
def clean_state_column(df):

    #help function for asserting that a value is not in the column state
    def assert_count(values, dataframe):
        for i in values:
            assert len(dataframe[dataframe["state"] == i]) == 0, "value count of " + i + " is greater 0"

    keep_states = ["failed","successful"]
    remove_states = ["undefined","suspended","live","canceled"]

    df["state"] = df["state"].astype("category")
    df = df[df.state.isin(keep_states)]
    try:
        assert_count(remove_states, df)
    except AssertionError as e:
        print("The operation failed")
        print(e)



    return df