#!/bin/python3
import os
import difflib

def find_directory_recursive(search_strings, dir_path):
    for root, dirs, files in os.walk(dir_path):
        for item in dirs:
            item_path = os.path.join(root, item)
            # search_stringsを含むまたは類似の名前を持つディレクトリを検索
            if search_strings in item or difflib.SequenceMatcher(None, item, search_strings).ratio() >= 0.8:
                return item_path

    # 見つからない場合はNoneを返す
    return None

search_strings = "TAHICHI"
dir_path = "/testDisk"
filename = find_directory_recursive(search_strings, dir_path)
print(filename)