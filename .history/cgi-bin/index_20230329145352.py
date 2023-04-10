#!/usr/bin/env python3
import datetime
from string import Template

try:
    with open('./index.html', 'r', encoding='utf-8') as f:
        html_template = Template(f.read())
except FileNotFoundError:
    print('Error: index.html not found')
    exit(1)

now_date = datetime.datetime.now().strftime('%Y年%m月%d日')
html_output = html_template.substitute(now=now_date)

print('Content-type: text/html\n')
print(html_output)
