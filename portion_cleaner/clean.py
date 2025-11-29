# Read feedback.txt → clean → save to new file.

import re,pandas as pd
txt='dirty.txt'
df=pd.read_csv(txt,sep='|')

removal=r'[!@#$%^&*<>.();:,.?'']'

df['Comment']=df['Comment'].replace(removal,'',regex=True)
print(df['Comment'])

df.to_csv('cleaned.csv',index=False)
