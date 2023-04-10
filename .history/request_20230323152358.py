import requests
from bs4 import BeautifulSoup

# Google検索ページのURL
url = 'https://www.google.com/search?q=python'

# HTTPヘッダー
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# GETリクエストを送信してHTMLを取得
response = requests.get(url, headers=headers)

# HTMLをBeautifulSoupで解析
soup = BeautifulSoup(response.text, 'html.parser')

# 検索結果のタイトルとURLを取得
for result in soup.find_all('div', class_='r'):
    title = result.find('h3').text
    link = result.find('a')['href']
    print(title)
    print(link)