#!/bin/python3 
import requests
from bs4 import BeautifulSoup


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
input_text = input("検索キーワードを入力してください：")
# Chromeドライバーを読み込み
#driver = webdriver.Chrome()

# Googleトップページにアクセス
driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS")

# <input>タグを指定する
input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')

# 入力するテキストを指定する
#input_text = "X12"
# 検索するキーワードを入力してください
input_text = input("検索キーワードを入力してください：")

# <input>タグにテキストを入力する
input_element.send_keys(input_text)

# # 検索ボックスにキーワードを入力して検索
# search_box = driver.find_element(By.NAME,"q")
# search_box.send_keys("AI")
# time.sleep(1)
# search_box.submit()
 time.sleep(10)
# # ブラウザを閉じる
#driver.quit()
