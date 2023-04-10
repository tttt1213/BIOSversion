#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser
import glob

def get_path(MB):
    fullpath=""
    target =MB.lower()
    default_path = "/testDisk/*"
    files=glob.glob(default_path)

    for file in files:
        print (target,file.lower())
        if target in file.lower():
            fullpath = file
    return fullpath

def get_tree(path):
    cmd = "tree " + path + " -H "+ path  + " --nolinks"
    pre_html = subprocess.run(cmd,shell=True, capture_output=True).stdout
    soup = bs(pre_html,'html.parser')
    soup.body.h1.extract()
    return soup
