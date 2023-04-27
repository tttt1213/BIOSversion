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
        self.df = mdb.read_table(dbpath, dbname)
        
    
    def cleaning(self):
        self.df["brand"] = self.df["name"].str.split(" ", n=1).str.get(0)
        self.df["product name"] = self.df["name"].str.split(" ", n=1).str.get(1)
        self.df["link"] = "<a href='result.py?BRAND=" + self.df["brand"] + "&MB=" + self.df["product name"] + "'>Search</a>"
        pd.set_option("display.max_rows", None)
        self.df = self.df.to_html(escape=False)
        return self.df

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