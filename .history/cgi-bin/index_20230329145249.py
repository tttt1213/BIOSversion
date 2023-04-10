#!/usr/bin/env python3
import datetime
from string import Template

# 現在時刻を文字列で取得
nowDate = datetime.datetime.now().strftime('%Y年%m月%d日')

# html を読み込み テンプレート文字列 にする
file_path = '../index.html'
with open(file_path, 'r', encoding="utf-8") as f:
    html_template = Template(f.read())

# HTML用のヘッダー情報とページの内容を出力
print('Content-type: text/html\n')
print(html_template.substitute(now=nowDate))