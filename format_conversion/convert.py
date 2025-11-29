import json
import pandas as pd

# file=json.loads('sample1.json')
with open('sample1.json','r') as f:
    file=json.load(f)

lst_dict={k:[v] for k ,v in file.items()}  #[v] : values must be in list form -> becase values are whole column's rows. not just a single row.
df=pd.DataFrame(lst_dict)

df.to_csv('my_sample.csv',index=False)
print('file is converted successfully.')
