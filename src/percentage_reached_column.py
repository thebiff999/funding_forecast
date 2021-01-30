#print(df.usd_pledged_real.tail( n = 5) )                                           #data inspection
#print(df.goal.tail(n = 5))
#df['percentage_reached_real'] = df['usd_pledged_real']/df['usd_goal_real']         #new column with
#print(df['percentage_reached_real'].tail(n = 5))                                   #data inspection

def add_column(df):
    df['percentage_reached_real'] = df['usd_pledged_real']/df['usd_goal_real']

    try:
        assert df['percentage_reached_real'].isna().sum() == 0
    except AssertionError as e:
        print("Adding the percentage_reached_real column has faield")
        print(e)
        
    return df