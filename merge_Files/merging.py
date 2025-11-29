# Merge two CSV files into one.
import pandas as pd

file1='dirty.txt'
file2='cleaned.csv'

df1=pd.read_csv(file1,sep='|')


df2=pd.read_csv(file2)

merged_file=pd.concat([df1['Comment'],df2['Comment']],ignore_index=True)

print(merged_file)
merged_file.to_csv('comments_merged.csv',index=False)
