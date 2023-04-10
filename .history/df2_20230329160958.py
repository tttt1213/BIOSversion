#!/bin/python3
import pandas as pd

# サンプルのデータフレームを作成
df = pd.DataFrame({'名前': ['Alice', 'Bob', 'Charlie'],
                   '年齢': [24, 32, 45],
                   '性別': ['女性', '男性', 'その他']})

# データフレームをHTMLに変換
html = df.to_html()
print(html)