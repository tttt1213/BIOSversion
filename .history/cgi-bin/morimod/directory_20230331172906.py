#!/bin/python3
import subprocess
from bs4 import BeautifulSoup as bs

def get_tree(MB):
    cmd = "tree /testDisk/" + MB + "-H /testDisk/"+ MB 
    runcmd = subprocess.call(cmd.split())
    print(runcmd)
    soup = bs(runcmd)
    soup = soup.find('html').decompose()

    print("--------------------------------------------------------------------")
    print(soup)
    return soup
