#!/bin/python3

import pandas as pd
from string import Template
import sys
import pandas_access as mdb
import datetime

dbpath = "/mnt/mori/test.mdb"
dbname = "test1"

class table():
    
    #アクセスファイルを読み込むdfで返す
    def create(self, dbpath, dbname):
        #Accessファイルからテーブル読み込み
        df = mdb.read_table(dbpath, dbname)
        return df
    
    def cleaning(self, dbpath, dbname):
        df = self.create(dbpath,dbname)
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
        with open('../main.html', 'r', encoding='utf-8') as f:
            html_template = Template(f.read())

        #htmlにdf流し込み
        html = html_template.substitute(now=now,df=df)
        print (html)
        return html



main_table = table()
main_table.html(dbpath,dbname)