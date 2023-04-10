#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser


def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB  + " --nolinks"
    pre_html = subprocess.run(cmd,shell=True, capture_output=True).stdout
    soup = bs(pre_html,'html.parser')
    
    # pタグを削除する
    #for p in soup.select('p'):
        #p.extract()



    #for html in soup.select('html'):
    #    html.extract()
    soup = soup.body.extract()
    
    #h1タグを削除する
    for h1 in soup.select('h1'):
        html = h1.extract()
    return html
