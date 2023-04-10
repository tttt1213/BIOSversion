#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser

def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB 
    #pre_html = subprocess.call(cmd.split())
    pre_html = '''
    <div>
        <p>Soup</p>
    </div>
    '''
    print(pre_html,lxml)
    soup = bs(pre_html)
    soup = soup.find('p').decompose()
    print (soup)
    return soup
