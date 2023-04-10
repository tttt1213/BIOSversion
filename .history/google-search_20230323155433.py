#!/bin/python3
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
search_box = driver.ffind_element(By.NAME,""q")
search_box.send_keys("AI")
search_box.submit()

# ブラウザを閉じる
driver.quit()
