#!/bin/python3

import pandas as pd
from string import Template
import pandas_access as mdb
import datetime

class Table:
    
    #アクセスファイルを読み込むdfで返す
    def create(self, dbpath, dbname):
        #Accessファイルからテーブル読み込み
        self.df = pd.DataFrame()
        self.df = mdb.read_table(dbpath, dbname)
       
    
    def add_columns(self):
        self.df["brand"] = self.df["name"].str.split(" ", n=1).str.get(0)
        self.df["product name"] = self.df["name"].str.split(" ", n=1).str.get(1)
        self.df["link"] = "<a href='result.py?BRAND=" + self.df["brand"] + "&MB=" + self.df["product name"] + "'>Search</a>"
    
    def to_html(self):
        pd.set_option("display.max_rows", None)
        html = self.df.to_html(escape=False)
        return html

    #リストをhtmlでプリント
    def html(self,dbpath,dbname):
        #時刻取得
        now = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')

        #createメソッドでdf作成
        self.create(dbpath,dbname)
        
        # cleaning
        self.add_columns()

        #htmlテンプレート読み込み
        with open('main.html', 'r', encoding='utf-8') as f:
            html_template = Template(f.read())

        #htmlにdf流し込み
        html = html_template.substitute(now=now,df=self.to_html())
        return html


dbpath = "/mnt/mori/test.mdb"
dbname = "test1"

main_table = Table()
html_content = main_table.html(dbpath, dbname)
print(html_content)
