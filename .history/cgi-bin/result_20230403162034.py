#!/usr/bin/env python3
import cgi

import sys
import morimod.search as search
import morimod.directory as directory

# URLパラメーターの取得
form = cgi.FieldStorage()
MB = form.getvalue("MB")
BRAND = form.getvalue("BRAND")

#BIOS BMCの最新ファイル名とバージョン取得（タプル型） search関数
BIOS=search.BIOS(MB)
BMC=search.BMC(MB)

print(BIOS)
print(BMC)

#MBのtestdirectoryのツリー取得(自作のget_tree関数)
tree = directory.get_tree(MB)

data={}
data = {
"MBname" : MB,
"MBlinl" : 
"BIOS_filename" : BIOS[0],
"BIOS_ver" : BIOS[1],
"BMC_filename" : BMC[0],
"BMC_ver" : BMC[1],
"tree" : tree
}

#reslut.htmlをテンプレートファイルとして値を埋め込む
with open("result.html", "r") as f:
    html_template = f.read()

html = html_template.format(**data)

print("Content-Type: text/html; charset=utf-8")
print()
print(html)
