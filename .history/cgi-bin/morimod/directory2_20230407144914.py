#!/bin/python3
import subprocess
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser

class TDtree:
    
    def __init__(self,MB):
        self.MB=MB
        self.sp="/testDisk/"
        self.stdout=""
        
    def setMB(self,MB):
        self.MB=MB
    
    def getMB(self):
        return self.MB

    def getPATH(self):
        cmd = "find {} -iname {} -type d -print|xargs -0 -n 1 echo -n".format(self.sp,self.MB)
        self.stdout=subprocess.run(cmd,shell=True, capture_output=True).stdout
        return  self.stdout

"""
    def get_tree(PATH):
        cmd = "tree {} -H {} --nolinks".format(PATH,PATH)
        pre_html = subprocess.run(cmd,shell=True, capture_output=True).stdout
        soup = bs(pre_html,'html.parser')
        soup.body.h1.extract()
        return soup
"""