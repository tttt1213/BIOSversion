#!/usr/bin/env python3
import cgi
from morimod import bios-search
from morimod import bmc-search

print("Content-type: text/html; charset=UTF-8")
# パラメーターの取得
form = cgi.FieldStorage()
MB = form.getvalue("MB")

htmlText = '''
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
<p>BIOS:{}</p>
<p>BMC:{}</p>
</div>
</body>
</html>

'''
BIOS=bios-search(MB)
BMC=bmc-search(MB)

print(htmlText.format(MB,BIOS,BMC))
