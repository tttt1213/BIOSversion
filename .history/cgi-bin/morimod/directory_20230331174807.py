#!/bin/python3
import subprocess
from bs4 import BeautifulSoup as bs

def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB 
    runcmd = subprocess.call(cmd.split())
    soup = bs(runcmd)
    soup = soup.find_all('html').decompose()
    return soup
