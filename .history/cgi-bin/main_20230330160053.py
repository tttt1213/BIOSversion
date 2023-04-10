#!/usr/bin/env python3
import cgi

# ヘッダーの設定
print("Content-type: text/html\n\n")

# パラメーターの取得
form = cgi.FieldStorage()
MB = form.getvalue("MB")


htmlText = '''Content-type: text/html; charset=UTF-8
<html>
<head>
<title>CGIパラメータの取得</title>
</head>
<body>
<header class="header">
<p>取得したパラメータ</p>
</header>
<div class="content">
<p>MB:{}</p>
</div>
</body>
</html>
'''
print(htmlText.format(MB))
