import os
import difflib

def find_similar_file(dir_path, file_name):
    # ディレクトリ内のファイルやディレクトリ名をリストで取得
    listA = os.listdir(dir_path)

    # ファイル名Aと一致するものまたは類似するファイル名が含まれる場合はそのファイルのフルパスを取得
    for item in listA:
        # ファイル名が一致する場合
        if item == file_name:
            file_path = os.path.join(dir_path, item)
            return file_path

        # ファイル名が類似する場合
        similarity_ratio = difflib.SequenceMatcher(None, item, file_name).ratio()
        if similarity_ratio >= 0.8:
            file_path = os.path.join(dir_path, item)
            return file_path

    # 一致するまたは類似するものがない場合
    return "Nothing"
path = "/testDisk"
file = "2019U-TRT"

find_similar_file(/testDisk,)