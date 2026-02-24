import pandas as pd 

df = pd.read_csv('data/clean_chat.csv')

df['Tanggal'] = pd.to_datetime(df['Tanggal'])

df_januari=df[df['Tanggal'].dt.month==1]

print(df_januari.head())