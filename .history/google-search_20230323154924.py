from selenium import webdriver

# Chromeドライバーを読み込み
driver = webdriver.Chrome()

# Googleトップページにアクセス
driver.get("https://www.google.com")

# 検索ボックスにキーワードを入力して検索
search_box = driver.find_element_by_name("q")
search_box.send_keys("AI")
search_box.submit()

# ブラウザを閉じる
driver.quit()
