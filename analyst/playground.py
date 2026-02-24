import pandas as pd

df = pd.read_csv('data/clean_chat.csv')

df['Tanggal'] = pd.to_datetime(df['Tanggal'])

df_januari=df[df['Tanggal'].dt.month==1]

pd.set_option('display.max_columns', None)


pd.set_option('display.width', 1000)

print(df_januari[['Tanggal', 'Pengirim', 'Pesan']].head())