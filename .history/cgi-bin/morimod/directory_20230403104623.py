#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser
import lxml

def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB 
    pre_html = subprocess.call(cmd.split())
    soup = bs(pre_html.content,'html.parser')
    html = soup.html.clear()
    
    return html
