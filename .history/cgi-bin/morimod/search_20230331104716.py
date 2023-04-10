#!/bin/python3 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def BIOS(MB):
    
    # Chromeドライバーを読み込み
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # SuperMicro [BIOS] ページにアクセス
    driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS")

    # <input>タグを指定する
    input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')

    # <input>タグにMB名を入力する
    input_element.send_keys(MB)

    #BIOSファイル名 htmlから指定
    file_element = driver.find_elements(By.XPATH, "//*[contains(@href, 'SoftwareItemID')]")

    # テキストを取得する
    for elem in file_element:
        if "zip" in elem.text :
        filename=elem.text

    ver_element = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/div[2]/table/tbody/tr/td[2]')
    ver = file_element.text

    return ver,filename



#MBのBMCバージョンを返す
def BMC(MB):


    # Chromeドライバーを読み込み
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    # SuperMicro [BMC] ページにアクセス
    driver.get("https://www.supermicro.com/support/resources/bios_ipmi.php?type=BMC")

    # <input>タグを指定する
    input_element = driver.find_element(By.XPATH,'//input[@type="search" and @aria-controls="DataTables_Table_0"]')
    # <input>タグにMB名を入力する
    input_element.send_keys(MB)


    #BIOSファイル名 find
    file_element = driver.find_elements(By.XPATH, "//*[contains(@href, 'SoftwareItemID')]")

    # テキストを取得する
    for elem in file_element:
        if "zip" in elem.text :
        filename=elem.text

    ver_element =  driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/div[2]/table/tbody/tr/td[2]')
    ver = file_element.text
    return ver,filename



