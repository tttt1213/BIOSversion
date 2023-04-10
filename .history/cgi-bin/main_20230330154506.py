#!/usr/bin/env python3
 
htmlText = '''Content-type: text/html; charset=UTF-8
 
<html>
<head>
  <title>CGIパラメータの取得</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
<header class="header">
   <p>取得したパラメータ</p>
</header>
<div class="content">
<p>%s(%s)さん、よろしくお願いします。</p>
</div>
</body>
</html>
'''
 
import cgi
 
form = cgi.FieldStorage()
MB = form.getvalue('MB','')

print(htmlText % (MB))
