#!/bin/python3

import pandas as pd
from string import Template
import sys
import pandas_access as mdb
import datetime

class table():

    def create(self, dbpath, dbname):
        self.db = mdb.read_table(dbpath, dbname)
        df = self.db
        df["brand"] = df["name"].str.split(" ", n=1).str.get(0)
        df["product name"] = df["name"].str.split(" ", n=1).str.get(1)
        df["link"] = "<a href='result.py?BRAND=" + df["brand"] + "&MB=" + df["product name"] + "'>Search</a>"
        pd.set_option("display.max_rows", None)
        df = df.to_html(escape=False)
        return df
    
    #リストをhtmlでプリント
    def html(self,dbpath,dbname):
        #時刻取得
        now = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')
        
        #createメソッドでdf作成
        mytable=table()
        df = mytable.create(dbpath,dbname)

        #htmlテンプレート読み込み
        with open('main.html', 'r', encoding='utf-8') as f:
            html_template = Template(f.read())
        
        #htmlにdf流し込み
        html = html_template.substitute(now=now,df=df)
        print (html)
        return html

table.ht,l("/mnt/mori/test.mdb","test1")

