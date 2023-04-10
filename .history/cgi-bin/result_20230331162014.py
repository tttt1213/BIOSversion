#!/usr/bin/env python3
import cgi
import morimod.search as search

# パラメーターの取得
form = cgi.FieldStorage()
MBname = form.getvalue("MB")

with open("result.html", "r") as f:
    html_template = f.read()

BIOS=search.BIOS(MB)
BMC=search.BMC(MB)

data = {
BIOS_filename : BIOS[0]
BIOS_ver : BIOS[1]
BMC_filename : [0]
BMC_ver : [1]
}

html = html_template.format(**data)
print("Content-Type: text/html; charset=utf-8")
print()
print(html)
