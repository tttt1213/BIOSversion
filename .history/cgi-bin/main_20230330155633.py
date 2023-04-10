#!/usr/bin/env python3
import cgi

# ヘッダーの設定
print("Content-type: text/html\n\n")

# パラメーターの取得
form = cgi.FieldStorage()
MB = form.getvalue("MB")

# HTMLの出力
print("<html>")
print("<head>")
print("<title>GETメソッドのパラメーター表示</title>")
print("</head>")
print("<body>")
print("<h1>GETメソッドで渡されたパラメーター: {}</h1>".format(MB))
print("</body>")
print("</html>")