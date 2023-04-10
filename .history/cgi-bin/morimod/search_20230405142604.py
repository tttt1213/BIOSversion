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
    try:
        file_element = driver.find_element(By.XPATH, "//a[contains(@href, 'SoftwareItemID')]")
    except:
        file_element = None
    #file_elementにはpdfファイルなども含まれているので zipファイルのみ選択する。
    if file_element is None:
    
        filename = "No file Found"
        fileURL = "https://www.google.com/search?q={}+{}+BIOS".format(BRAND,MB)
        
    else:
        for elem in file_element:
            if "zip" in elem.text :
                filename = elem.text
                fileURL = elem.get_attribute('href')

    return filename,fileURL


#MBのBMCバージョンを返す
def BMC(BRAND,MB):

    # SuperMicro [BMC] ページにアクセス
    driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BMC")

    # <input>タグを指定する
    input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')

    # <input>タグにMB名を入力する
    input_element.send_keys(MB)

    try:
        file_element = driver.find_element(By.XPATH, "//a[contains(@href, 'SoftwareItemID')]")
    except:
        file_element = None
    #file_elementにはpdfファイルなども含まれているので zipファイルのみ選択する。
    if file_element is None:
    
        filename = "No file Found"
        fileURL = "https://www.google.com/search?q={}+{}+BMC".format(BRAND,MB)
        
    else:
        for elem in file_element:
            if "zip" in elem.text :
                filename = elem.text
                fileURL = elem.get_attribute('href')

    return filename,fileURL
    
#ブランド名とマザボ名を入力するとそのキーワードでgoogle検索し1番上のページを表示する。

def search_google(BRAND,MB):
    # WebDriverを起動する
    driver.get('https://www.google.com/')
    # キーワードを検索ボックスに入力してEnterキーを押す
    search_box = driver.find_element(By.NAME,'q')
    search_box.send_keys(BRAND + ' ' + MB)
    search_box.submit()
    #マザーボード名の文字列を含む見出しのリストを取得
    h = driver.find_elements(By.XPATH,"//h3[contains(text(),\"{}\")]".format(MB))
    
    #リストの中から1番最初のtyanページを返す
    for elem in h:
        TITLE = elem.text
        URL = elem.find_element(By.XPATH,"..").get_attribute("href")
        
        if MB in TITLE and  BRAND.lower() in URL:
            #print("{}:{}".format(title,URL))
            return title,URL
    else:
    # WebDriverを終了する
    driver.quit()
    return
