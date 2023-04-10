#!/bin/python3 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#MBのBMCバージョンを返す
def BMC_search(MB):


    # Chromeドライバーを読み込み
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # SuperMicro [BMC] ページにアクセス
    driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BMC")

    # <input>タグを指定する
    input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')
    # <input>タグにMB名を入力する
    input_element.send_keys(MB)


    #BIOSファイル名 find
    file_element = driver.find_element(By.XPATH,'//a[contains(text(), "BMC")]')
    # テキストを取得する
    filename = file_element.text

    ver_element = file_element = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/div[2]/table/tbody/tr/td[2]')
    ver = file_element.text
    return ver,filename


print(BMC_search("X12STL-F"))
