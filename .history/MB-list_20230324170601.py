#!/bin/python3
import pandas as pd
import pandas_access as mdb

pd.set_option('display.max_columns', 5)

# mdb から dataframe の取得
origdf = mdb.read_table("/mnt/mori/test.mdb", "test1")
print (origdf)
df = origdf['name'].str.split(' ', expand=True)
#df.columns = ['company','name']
print(df)