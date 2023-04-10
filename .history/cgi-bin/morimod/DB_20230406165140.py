#!/bin/python3
import pandas as pd
import pandas_access as mdb

db_path = '/mnt/mori/test.mdb'
# mdb から 有効マザーボードの情報(table1)取得
# df形式でhtmlにdf3.pyに渡す

def create_list():
    table_name = 'test1'
    dblist = mdb.read_table(db_path, table_name)
    return dblist


def format_list(list):
    df = pd.DataFrame()
    df["brand"] = list["name"].str.split(" ",n=1).str.get(0)
    df["product name"] = list["name"].str.split(" ",n=1).str.get(1)
    df["link"] = '<a href=\"result.py?BRAND=' + list["name"].str.split(" ",n=1).str.get(0) + '&MB=' + list["name"].str.split(" ",n=1).str.get(1) + '\">Find!</a>'
    pd.set_option("display.max_rows", None)
    return df

def get_list():
    list = create_list()
    list = format_list(list)
    return list
