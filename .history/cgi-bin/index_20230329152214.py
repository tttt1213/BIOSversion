#!/usr/bin/env python3

import datetime 
from string import Template
import sys

# HTMLファイルから読み込む
try:
    with open('../index.html', 'r', encoding='utf-8') as f:
        html_template = Template(f.read())
        print(html_template)
except FileNotFoundError:
    print('Error: index.html not found', file=sys.stderr)
    sys.exit(1)

# 現在の日付・時刻を取得する
now_date = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')

# テンプレートを置換してHTMLコードを生成する
html_output = html_template.substitute(now=now_date)

# HTMLのContent-typeを明示的に指定して出力する
print('Content-Type: text/html; charset=utf-8')
print()
print(html_output)
