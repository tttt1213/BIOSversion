#!/bin/python3
import subprocess
import requests
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser
import glob

def get_path(MB):
    target_file ="/testDisk/{}".format(MB)
    default_path = "/testDisk/*"
    files=glob.glob(default_path)
    for file in files:
        print(file)
        print(file.str.len() == target_file.str.len())
        if file.lower() ==  target_file.lower():
            fullpath = file
    return fullpath

def get_tree(path):
    cmd = "tree " + path + " -H "+ path  + " --nolinks"
    pre_html = subprocess.run(cmd,shell=True, capture_output=True).stdout
    soup = bs(pre_html,'html.parser')
    soup.body.h1.extract()
    return soup
