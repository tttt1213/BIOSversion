#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs

def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB 
    pre_html = subprocess.call(cmd.split())
    soup = bs(pre_html,"html_parser")
    soup = soup.find_all('html').decompose()
    return soup
