#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# ブラウザを起動する
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 対象のURLを読み込む
URL="https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS"
driver.get(URL)

# 検索対象の文字列を指定する
search_string = "X11DPi-N"


# <input>タグを指定する
input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')

# <input>タグにMB名を入力する
MB="X12DPi-N"
input_element.send_keys(MB)

# .zipを含む要素を探す
zip_elements = driver.find_elements_by_xpath("//*[contains(text(), '.zip')]")

# 見つかった要素を表示する
for elem in zip_elements:
    print(elem.text)

# ブラウザを閉じる
driver.quit()