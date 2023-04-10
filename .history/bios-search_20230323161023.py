#!/bin/python3 
import requests
from bs4 import BeautifulSoup


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://google.com')

# Chromeドライバーを読み込み
driver = webdriver.Chrome()

# 検索するキーワードを入力してください
search_term = input("検索キーワードを入力してください：")

# Googleトップページにアクセス
driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS")

# 検索ボックスにキーワードを入力して検索
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("AI")
time.sleep(1)
search_box.submit()
time.sleep(1)
# ブラウザを閉じる
driver.quit()
