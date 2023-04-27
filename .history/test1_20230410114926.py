#!/bin/python3
import os
import difflib

# ディレクトリパスとファイル名Aを定義
dir_path = "/testDisk"
file_name = "A"

# ディレクトリ内のファイルやディレクトリ名をリストで取得
listA = os.listdir(dir_path)

# ファイル名Aと一致するものまたは類似するファイル名が含まれる場合はそのファイルのフルパスを取得
for item in listA:
    # ファイル名が一致する場合
    if item == file_name:
        file_path = os.path.join(dir_path, item)
        print(file_path)
        continue

    # ファイル名が類似する場合
    similarity_ratio = difflib.SequenceMatcher(None, item, file_name).ratio()
    if similarity_ratio >= 0.8:
        file_path = os.path.join(dir_path, item)
        print(file_path)
