#!/bin/python3
import pyodbc

# データベースへの接続
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=/mnt/mori/test.mdb;'
conn = pyodbc.connect(conn_str)

# カーソルの作成
cursor = conn.cursor()

# クエリの実行
query = 'SELECT * FROM AAA'
cursor.execute(query)

# 結果の取得
rows = cursor.fetchall()

# テーブル形式で出力
for row in rows:
    print(row)