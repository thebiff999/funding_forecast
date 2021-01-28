#Welche Daten fehlen ?                                                                                               
                                                                                                                     
print(df.isnull().sum())                            #name has 4 missing values                                       
print(df[df.name.isnull()])                         #every row where name is NaN                                     
print(df.shape)                                     #shape of the df                                                 
df = df.dropna(subset=['name'])                     #dropping                                                        
print(df.shape)                                     #shape of df with NaN values removed (4 less thah in rows less)  
print(df[df.name.isnull()])                         #empty data frame for missing values in name (successful removal)
print(df.head(5))                                                                                                                                           