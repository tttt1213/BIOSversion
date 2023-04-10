#!/bin/python3
import pandas as pd
import pandas_access as mdb

# mdb から dataframe の取得
table = mdb.read_table("/mnt/mori/test.mdb", "test1")
print(table)

pd.set_option('display.max_rows', 500)
df = table['name'].str.split(' ',2)

#print(df)
#html = df.to_html()
#print (html)