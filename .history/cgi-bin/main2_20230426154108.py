#!/bin/python3

import pandas as pd
from string import Template
import sys
import pandas_access as mdb

class mytable():
    def __init__(self):
        print("init")
        with open('../main.html', 'r', encoding='utf-8') as f:
             html_template = Template(f.read())
    
        now_date = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')
        
    def create(self, dbpath, dbname):
        self.db = mdb.read_table(dbpath, dbname)
        df = self.db
        df["brand"] = df["name"].str.split(" ", n=1).str.get(0)
        df["product name"] = df["name"].str.split(" ", n=1).str.get(1)
        df["link"] = "<a href='result.py?BRAND=" + df["brand"] + "&MB=" + df["product name"] + "'>Search</a>"
        pd.set_option("display.max_rows", None)
        df = df.to_html(escape=False)
        return df
    
    def print_html():
        html_output = html_template.substitute(now=now_date,df=now_df)
        print(html_output)
        
