#!/bin/python3
import pandas as pd
import pandas_access as mdb

# mdb から dataframe の取得
df = mdb.read_table("/mnt/mori/test.mdb", "test1")
df = df['name'].str.split(' ', expand=True)
df.columns = ['company','name']
print(df)