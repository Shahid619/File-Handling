# Append new  record into CSV.

import pandas as pd

new_data={
    'fruit':['Orange','strawberry'],
    'size':['medium','small'],
    'color':['orange','Red']
}

df=pd.read_csv('my_sample.csv')

update=pd.DataFrame({k:v for k,v in new_data.items()})
updated_csv=pd.concat([df,update],ignore_index=True)

# ignore index : auto increase s.no.  ,[df,..] instead of (df,...)-> because single val expected ,so lst count as single value.
print(updated_csv)

# updated_csv.to_csv('updated.csv',index=False)
# print('file updated with values.')

