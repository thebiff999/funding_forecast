print(df.usd_pledged_real.tail( n = 5) )                                           #data inspection
print(df.goal.tail(n = 5))
df['percentage_reached_real'] = df['usd_pledged_real']/df['usd_goal_real']         #new column with
print(df['percentage_reached_real'].tail(n = 5))                                   #data inspection
