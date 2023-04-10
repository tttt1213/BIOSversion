#!/bin/python 

from selenium.webdriver.common.by import By
import re

# ブラウザを起動する
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
options = webdriver.ChromeOptions()

# 対象のURLを読み込む
URL="https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS"
driver.get(URL)

# 検索対象の文字列を指定する
search_string = "X11DPi-N"

# 対象の文字列を含む要素を検索する
elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{search_string}')]")

# リンクされたテキストを取得する
for element in elements:
    link_element = element.find_element(By.XPATH, "./following-sibling::td[1]/a")
    link_text = link_element.text
    if re.search(r"\.zip$", link_text):
        print(link_text)

# ブラウザを閉じる
driver.quit()