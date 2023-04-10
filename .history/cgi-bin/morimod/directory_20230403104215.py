#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser
import lxml

def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB 
    #pre_html = subprocess.call(cmd.split())
    pre_ht,l = """
    <!doctype html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>HTML Sample</title>
  <link rel="stylesheet" href="style.css">
  <script type="text/javascript" src="sample.js"></script>
</head>
<body>
  <div class="header">Header領域</div>
  <div class="main">
    <h1>見出し</h1>
    <p>コンテンツ</p>
    <img src="img/sample1.jpg">
  </div>
  <div class="footer">
    <span>Footer領域</span>
    <a href="#">リンク</a>
  </div>
</body>
</html>
    
    """
    
    print(pre_html)
    soup = bs(pre_html,'html.parser')
    soup = soup.html.extract()
    print (soup)
    return soup
