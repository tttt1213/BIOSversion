#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser


def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB 
    pre_html = subprocess.call(cmd.split())
    print("-------------------------------------------------------------------")
    print(pre_html)
    #soup = bs(pre_html,'html.parser')
    #html = soup.html.clear()
    
    return 