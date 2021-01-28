print(df.pledged.tail( n = 5) )                             #data inspection
print(df.goal.tail(n = 5))
df['percentage_reached'] = df['pledged']/df['goal']         #new column with percentage pledged
print(df['percentage_reached'].tail(n = 5))                 #data inspection