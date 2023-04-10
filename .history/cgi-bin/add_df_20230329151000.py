#!/bin/python3
import pandas as pd
import datetime
from string import Template

# データフレームを作成
now_df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})

try:
    with open('./index.html', 'r', encoding='utf-8') as f:
        html_template = Template(f.read())
except FileNotFoundError:
    print('Error: index.html not found')
    exit(1)

now_date = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')
html_output = html_template.substitute(df=now_df)

print('Content-type: text/html\n')
print(html_output)
