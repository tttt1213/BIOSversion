#!/bin/python3
import pandas as pd
import datetime
from string import Template
import sys

try:
    with open('df.html', 'r', encoding='utf-8') as f:
        html_template = Template(f.read())
except FileNotFoundError:
    print('Error: index.html not found', file=sys.stderr)
    sys.exit(1)


now_date = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')
# データフレームを作成
now_df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
now_df = now_df.to_html()

html_output = html_template.replace(df=now_df)

print('Content-type: text/html\n')
print(html_output)
