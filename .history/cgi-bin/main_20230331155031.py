#!/bin/python3
import pandas as pd
import datetime
from string import Template
import sys
from morimod import MBlist


print ()

try:
    with open('main.html', 'r', encoding='utf-8') as f:
        html_template = Template(f.read())
except FileNotFoundError:
    print('Error: index.html not found', file=sys.stderr)
    sys.exit(1)

now_date = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')

# データフレームを作成
now_df = DB.get_list()
now_df = now_df.to_html(escape=False)

html_output = html_template.substitute(now=now_date,df=now_df)
print(html_output)
