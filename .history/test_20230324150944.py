#!/bin/python3
import pyodbc
import pandas as pd

# データベースファイルのパスとODBCドライバーのパスを指定
db_path = "/mnt/test.mdb"
driver_path = "/usr/lib/x86_64-linux-gnu/odbc/libmdbodbc.so"

# ODBCドライバーを登録
pyodbc.pooling = False
pyodbc.autocommit = True
pyodbc.drivers()
pyodbc.register_driver('MDBTools', driver, unicode_results=True)

# ODBC接続文字列を作成
conn_str = 'DRIVER={MDBTools};DBQ=%s;' % db_path

# データベースに接続
cnxn = pyodbc.connect(conn_str)

# テーブルを読み込み
df = pd.read_sql('SELECT * FROM table1', cnxn)

# DataFrameを表示
print(df)