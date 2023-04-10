#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser
import lxml

def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB 
    #pre_html = subprocess.call(cmd.split())
    pre_html = '''
    <div>
        <p>Soup</p>
    </div>
    <head></head>
    '''
    print(pre_html)
    soup = bs(pre_html,,'lxml')
    soup = soup.find('p').decompose()
    print (soup)
    return soup
