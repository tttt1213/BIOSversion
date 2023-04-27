#!/bin/python3

import pandas as pd
import pandas_access as mdb

class table():

    #初期値設定
    def __init__(self):
        print("init")
        
    def create(self , dbpath , dbname):
        self.db = mdb.read_table(dbpath,dbname)
        df = self.db
        df["brand"] = list["name"].str.split(" ",n=1).str.get(0)
        df["product name"] = list["name"].str.split(" ",n=1).str.get(1)
        df["link"] = '<a href=\"result.py?BRAND=' + list["name"].str.split(" ",n=1).str.get(0) + '&MB=' + list["name"].str.split(" ",n=1).str.get(1) + '\">Search</a>'
        pd.set_option("display.max_rows", None)
        return df

main_table = table()
df = main_table.create("/mnt/mori/test.mdb","test1")
print(main_table)
