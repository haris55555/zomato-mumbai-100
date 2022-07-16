
pd.set_option('display_max_rows',100)
pd.set_options('display_max_columns',3)

df=pd.read_csv('TOP100.csv','r')
print(df[~df.duplicated(subset=['NAME'])])