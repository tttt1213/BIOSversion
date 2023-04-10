#!/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://google.com')

# Chromeドライバーを読み込み
driver = webdriver.Chrome()

# Googleトップページにアクセス
driver.get("https://www.google.com")

# 検索ボックスにキーワードを入力して検索
search_box = driver.find_element(By.CLASS_NAME,"gLFyf")
search_box.send_keys("AI")
search_box.submit()

time.sleep(60)
# ブラウザを閉じる
driver.quit()
