#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser


def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB 
    pre_html = subprocess.run(cmd,shell=True, capture_output=True).stdout
    soup = bs(pre_html,'html.parser')
    
    # pタグを削除する
    #for p in soup.select('p'):
        #p.extract()

    # h1タグを削除する
    #for h1 in soup.select('h1'):
        #h1.extract()

    #for html in soup.select('html'):
    #    html.extract()
    html = soup.body.extract()
    return html
