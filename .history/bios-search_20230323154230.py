import requests
from bs4 import BeautifulSoup

# 検索するキーワードを入力してください
search_term = input("検索キーワードを入力してください：")

# 検索フォームのURL
url = "https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS"

# 検索キーワードを含むURLを作成する
search_url = url + "&s=" + search_term

# リクエストを送信し、ページのHTMLを取得する
response = requests.get(search_url)
html = response.content

# BeautifulSoupを使用してHTMLをパースする
soup = BeautifulSoup(html, 'html.parser')

# 検索結果を取得する
results = soup.find_all('a', {'class': 'list-group-item'})

# 検索結果を表示する
print (results)