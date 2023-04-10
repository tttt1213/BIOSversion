#!/bin/python3
import pandas as pd
import pandas_access as mdb

pd.set_option('display.max_columns', 200)

# mdb から dataframe の取得
origdf = mdb.read_table("/mnt/mori/test.mdb", "test1")

pd.set_option('display.max_rows', 500)
df = origdf['name'].str.split(' ', expand=True)

pd.set_option('display.max_rows', 500)
print(df)
html = df.to_html()
print (html)