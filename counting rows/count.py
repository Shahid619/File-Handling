# Read customers.csv → count number of rows.

import pandas as pd

df=pd.read_csv('orders.csv')
print(f'number of rows : {len(df)}')
