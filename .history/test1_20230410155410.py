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

def find_directory_with_highest_similarity(search_strings):
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

search_strings = "1029GQ-"
dir_path = "/testDisk"

list = find_directories_recursive(search_strings, dir_path)
highestfile = find_directory_with_highest_similarity(search_strings, dir_path)

print(list)
print (highestfile)