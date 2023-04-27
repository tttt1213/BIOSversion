#!/bin/python3
import os
import difflib


def find_directories_recursive(search_strings, dir_path):
    matching_dirs = []
    for root, dirs, files in os.walk(dir_path):
        for item in dirs:
            item_path = os.path.join(root, item)
            # search_stringsを含むまたは類似の名前を持つディレクトリを検索
            if search_strings in item or difflib.SequenceMatcher(None, item, search_strings).ratio() >= 0.8:
                matching_dirs.append(item_path)

    # マッチングするディレクトリがなければ空リストを返す
    return matching_dirs

search_strings = "B550"
dir_path = "/testDisk"

filename = find_directories_recursive(search_strings, dir_path)
print(filename)