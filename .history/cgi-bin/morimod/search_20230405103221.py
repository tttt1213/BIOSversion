#!/bin/python3 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)


def BIOS(BRAND,MB):
    # Chromeドライバーを読み込み

    # SuperMicro [BIOS] ページにアクセス
    driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS")

    # <input>タグを指定する
    input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')
    # <input>タグにMB名を入力して絞り込む
    input_element.send_keys(MB)
    
    #MBのBIOSファイル名をfindする
    #hrefにSoftwareItemIDを含む要素を取得する。
    file_element = driver.find_element(By.XPATH, "//a[contains(@href, 'SoftwareItemID')]")

    #file_elementにはpdfファイルなども含まれているので zipファイルのみ選択する。
    
    if file_element is not None:
    
        filename = "No file Found"
        fileURL = "https://www.google.com/search?q={}%20{}".format(BRAND,MB)
        
    else:
        for elem in file_element:
            if "zip" in elem.text :
                filename = elem.text
                fileURL = elem.get_attribute('href')

    

    return filename,fileURL


#MBのBMCバージョンを返す
def BMC(MB):
    # SuperMicro [BMC] ページにアクセス
    driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BMC")

    # <input>タグを指定する
    input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')

    # <input>タグにMB名を入力する
    input_element.send_keys(MB)

    #BIOSファイル名 find
    file_element = None
    file_element = driver.find_elements(By.XPATH, "//*[contains(@href, 'SoftwareItemID')]")
    
    if file_element is None:
            filename = "NOT Find In Supermicro "
            fileURL =  "https://www.google.com/search?q=" + MB

    #file_elementにはpdfファイルなども含まれているので zipファイルのみ選択する。
    for elem in file_element:
        if "zip" in elem.text :
            filename = elem.text
            fileURL = elem.get_attribute('href')

    return filename,fileURL

    
#ブランド名とマザボ名を入力するとそのキーワードでgoogle検索し1番上のページを表示する。

def search_google(keyword1, keyword2):
    # WebDriverを起動する
    
    driver.get('https://www.google.com/')
    
    # キーワードを検索ボックスに入力してEnterキーを押す
    search_box = driver.find_element(By.NAME,'q')
    search_box.send_keys(keyword1 + ' ' + keyword2)
    search_box.submit()

    # 検索結果の最初のリンクを取得する
    first_link = driver.find_element(By.XPATH, "//a[contains(@href, 'www.supermicro.com')]")
    url = first_link.get_attribute('href')
    
    # WebDriverを終了する
    driver.quit()
    
    return url
