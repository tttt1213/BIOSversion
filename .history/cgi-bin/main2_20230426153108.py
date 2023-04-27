#!/bin/python3

import pandas as pd
import datetime
from string import Template
import sys
from morimod import DB
import pandas_access as mdb
import pandas as pd
from string import Template
import sys
import pandas_access as mdb

class mytable():
    def __init__(self):
        print("init")
        
    def create(self, dbpath, dbname):
        self.db = mdb.read_table(dbpath, dbname)
        df = self.db
        df["brand"] = df["name"].str.split(" ", n=1).str.get(0)
        df["product name"] = df["name"].str.split(" ", n=1).str.get(1)
        df["link"] = "<a href='result.py?BRAND=" + df["brand"] + "&MB=" + df["product name"] + "'>Search</a>"
        pd.set_option("display.max_rows", None)
        return df

main_table = mytable()
df = main_table.create("/mnt/mori/test.mdb", "test1")
print(df)
