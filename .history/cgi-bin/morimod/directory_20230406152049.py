#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser

def get_path(MB):
    cmd = "ls /testDisk"
    list = subprocess.run(cmd,shell=True, capture_output=True).stdout
    for i in list:
            print (i)

def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB  + " --nolinks"
    pre_html = subprocess.run(cmd,shell=True, capture_output=True).stdout
    soup = bs(pre_html,'html.parser')
    soup.body.h1.extract()
    return soup
