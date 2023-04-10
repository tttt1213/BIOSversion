#!/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://google.com')

# Chromeドライバーを読み込み
driver = webdriver.Chrome()

# Googleトップページにアクセス
driver.get("https://www.google.com")

# 検索ボックスにキーワードを入力して検索
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("AI")
time.sleep(1)
search_box.submit()
time.sleep(1)
# ブラウザを閉じる
driver.quit()
