#!/usr/bin/env python3 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Helper function to fetch data from the webpage
def get_data(URL, search_term):
    with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
        driver.get(URL)
        input_element = driver.find_element(By.XPATH,"//input[@type='search']")
        input_element.send_keys(search_term)
        file_element = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0_filter"]/label/input, "' + search_term.upper() + '")]')
        ver_element = file_element.find_element(By.XPATH,'./parent::td/following-sibling::td[1]')
        return ver_element.text, file_element.text

#MBのBIOSバージョンを返す
def BIOS(MB):
    URL = "https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS"
    search_term = 'bios'
    return get_data(URL, search_term)

#MBのBMCバージョンを返す
def BMC(MB):
    URL = "https://www.supermicro.com/support/resources/bios_ipmi.php?type=BMC"
    search_term = 'bmc'
    return get_data(URL, search_term)
