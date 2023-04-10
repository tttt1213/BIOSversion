#!/usr/bin/env python3
import cgi
import sys
import morimod.search as search
import morimod.directoly

# パラメーターの取得
form = cgi.FieldStorage()
MB = form.getvalue("MB")

with open("result.html", "r") as f:
    html_template = f.read()

BIOS=search.BIOS(MB)
BMC=search.BMC(MB)
print(BIOS)
print(BMC)
tree = directory.get_tree()


data={}
data = {
"MBname" : MB,
"BIOS_filename" : BIOS[0],
"BIOS_ver" : BIOS[1],
"BMC_filename" : BMC[0],
"BMC_ver" : BMC[1]
}

html = html_template.format(**data)

print("Content-Type: text/html; charset=utf-8")
print()
print(html)
