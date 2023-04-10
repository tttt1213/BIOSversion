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

# <input>タグを指定する
input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')

# <input>タグにMB名を入力する
MB="X11DPi-N"
input_element.send_keys(MB)

elements = driver.find_elements(By.XPATH, '//a[contains(text(),"SoftwareItemID")]')

for elem in elements:
    print(elem.text)

# ブラウザを閉じる
driver.quit()