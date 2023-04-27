#!/bin/python3
import subprocess
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser
import glob
import os
import difflib

"""
def get_path(MB):
    fullpath="Nothing"
    target =MB.lower()
    default_path = "/testDisk/*"
    files=glob.glob(default_path)

    for file in files:
        if target in file.lower():
           fullpath = file
    return fullpath
"""

def get_path(search_strings):
    dir_path="/testDisk"
    matching_dirs = []
    max_similarity = 0
    for root, dirs, files in os.walk(dir_path):
        for item in dirs:
            item_path = os.path.join(root, item)
            # search_stringsを含むまたは類似の名前を持つディレクトリを検索
            similarity = difflib.SequenceMatcher(None, item, search_strings).ratio()
            if search_strings in item or similarity >= 0.8:
                if similarity > max_similarity:
                    matching_dirs = [item_path]
                    max_similarity = similarity
                elif similarity == max_similarity:
                    matching_dirs.append(item_path)

    if matching_dirs:
        # マッチングするディレクトリがある場合は一致度が最も高いものを返す
        return matching_dirs[0]
    else:
        # マッチングするディレクトリがなければNoneを返す
        return None


def get_tree(PATH):
    cmd = "tree {} -H {} --nolinks".format(PATH,PATH)
    pre_html = subprocess.run(cmd,shell=True, capture_output=True).stdout
    soup = bs(pre_html,'html.parser')
    soup.body.h1.extract()
    return soup
