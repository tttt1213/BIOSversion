#!/bin/python3
import pandas as pd
import pandas_access as mdb

# mdb から dataframe の取得
def return_MBlist():
    db_path = '/mnt/mori/test.mdb'
    table_name = 'test1'
    dblist = mdb.read_table(db_path, table_name)
    df=pd.DataFrame()
    df["brand"] = dblist["name"].str.split(" ",n=1).str.get(0)
    df["product name"] = dblist["name"].str.split(" ",n=1).str.get(1)
    df["link"]= "test" + df["product_name"] + "test"
    pd.set_option("display.max_rows", None)
    
    return df
