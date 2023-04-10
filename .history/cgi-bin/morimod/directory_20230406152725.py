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
            if file.lower() ==  target_file.lower() #ディレクトリには大文字小文字混在しているためすべて小文字に変換して判定
            return file
    return None
def get_tree(MB):
    cmd = "tree /testDisk/" + MB + " -H /testDisk/"+ MB  + " --nolinks"
    pre_html = subprocess.run(cmd,shell=True, capture_output=True).stdout
    soup = bs(pre_html,'html.parser')
    soup.body.h1.extract()
    return soup
