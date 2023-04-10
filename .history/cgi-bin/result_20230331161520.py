#!/usr/bin/env python3
import cgi
import morimod.search as search

# パラメーターの取得
form = cgi.FieldStorage()
MB = form.getvalue("MB")

with open("result.html", "r") as f:
    template = f.read()
htmlText = '''
<html>
<head>
<title></title>
</head>
<body>
<header class="header">
</header>
<div class="content">
<p>MB:{}</p>
<p>BIOS:<a href="{}">{}<a/></p>
<p>BMC:<a href="{}">{}<a/></p>
</div>
</body>

</html>

'''
BIOS=search.BIOS(MB)
BMC=search.BMC(MB)

print(htmlText.format(MB,BIOS[1],BIOS[0],BMC[1],BMC[0]))
