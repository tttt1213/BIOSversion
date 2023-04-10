#!/bin/python3
import pandas as pd

def add_dataframe_to_html(file_path, df):
    
    file_path='./index.html'
    df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})

    # テンプレートファイルを読み込む
    with open(file_path, 'r') as f:
        html_text = f.read()

    # データフレームをHTML形式に変換する
    df_html = df.to_html()

    # データフレームをHTMLテンプレートファイルに挿入する
    new_html_text = html_text.replace('{{ dataframe }}', df_html)

    # 更新されたHTMLをファイルに保存する
    with open(file_path, 'w') as f:
        f.write(new_html_text)
