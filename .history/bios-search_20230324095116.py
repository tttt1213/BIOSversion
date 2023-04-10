#!/bin/python3 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

MB="X12STL-F"

# Chromeドライバーを読み込み
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# SuperMicro [BIOS] ページにアクセス
driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS")

# <input>タグを指定する
input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')

# <input>タグにMB名を入力する
input_element.send_keys(MB)


#BIOSファイル名取得
a_element = driver.find_element_by_xpath('//a[contains(text(), "BIOS")]')

# テキストを取得する
text = a_element.text



# search_box.submit()
input("終わり")