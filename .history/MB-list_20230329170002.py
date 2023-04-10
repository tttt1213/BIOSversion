#!/bin/python3
import pandas as pd
import pandas_access as mdb

# mdb から dataframe の取得
def MB-list():
    table = mdb.read_table("/mnt/mori/test.mdb", "test1")
    df=pd.DataFrame()
    df['brand'] = table['name'].str.split(" ").str.get(0)
    df['product name'] = table['name'].str.split(" ").str.get(1)
    df['etc'] = table['name'].str.split(" ").str.get(2)

    pd.set_option('display.max_rows', None)
    return df
