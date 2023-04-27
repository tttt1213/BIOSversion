#!/usr/bin/env python3
import cgi
import morimod.search as search
import morimod.directory as directory
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)


# URLパラメーターの取得
form = cgi.FieldStorage()
MB = form.getvalue("MB")
BRAND = form.getvalue("BRAND")

class result:
    def __init__(self,BRAND.MB):
        self.BRAND = BRAND
        self.MB = MB
        self.google=

    def search_url():
        self.google= "https://www.google.com/"
        driver.get(self.google)
        # キーワードを検索ボックスに入力してEnterキーを押す
        search_box = driver.find_element(By.NAME,'q')
        search_box.send_keys(BRAND + ' ' + MB)
        search_box.submit()
        #マザーボード名の文字列を含む見出しのリストを取得
        h = driver.find_elements(By.XPATH,"//h3[contains(text(),\"{}\")]".format(MB))
        #リストの中から1番最初のページを返す
        TITLE = h[0].text
        URL = h[0].find_element(By.XPATH,"..").get_attribute("href")
        return TITLE,URL
    
    
#公式ページ検索
url=search.search_google(BRAND,MB)
#BIOS BMCの最新ファイル名とバージョン取得（タプル型） search関数
BIOS=search.BIOS(BRAND,MB)
BMC=search.BMC(BRAND,MB)


#MBのtestdirectoryのツリー取得(自作のget_tree関数)
PATH = directory.get_path(MB)
tree = directory.get_tree(PATH)

data={}
data = {
"MBname" : MB,
"url" : url[1],
"BIOS_filename" : BIOS[0],
"BIOS_ver" : BIOS[1],
"BMC_filename" : BMC[0],
"BMC_ver" : BMC[1],
"tree" : tree
}

#reslut.htmlをテンプレートファイルとして値を埋め込む
with open("result.html", "r") as f:
    html_template = f.read()

html = html_template.format(**data)

print("Content-Type: text/html; charset=utf-8")
print()
print(html)
