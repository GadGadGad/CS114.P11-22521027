import sys
import pandas as pd
import time

# start = time.time()

df = pd.read_csv(sys.stdin, usecols=['CustomerID', 'InvoiceDate'], encoding='unicode_escape', encoding_errors='replace').drop_duplicates()

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df = df.groupby('CustomerID')['InvoiceDate'].max().reset_index().sort_values(by='CustomerID')

df['score'] = (df['InvoiceDate'] - df['InvoiceDate'].min()).dt.days
df = df[['CustomerID', 'score']]

sys.stdout.write(df.to_string(index=False, justify='end'))

# end = time.time()

# # print(f'{end - start}s')
