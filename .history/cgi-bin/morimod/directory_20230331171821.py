#!/bin/python3
import subprocess
from bs4 import BeautifulSoup as soup

def get_tree(MB):
    cmd = "tree  /testDisk/"+MB
    runcmd = subprocess.call(cmd.split())
    soup = BeautifulSoup(runcmd, 'html.parser')
    soup = soup.find('head').decompose()
    soup = soup.find('title').decompose()
    return 
