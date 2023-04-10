#!/bin/python3
import subprocess
from bs4 import BeautifulSoup as bs
def get_tree(MB):
    cmd = "tree  /testDisk/"+MB
    runcmd = subprocess.call(cmd.split())
    soup = bs(runcmd, 'html.parser')
    soup = soup.find('head').decompose()
    soup = soup.find('title').decompose()
    return soup
