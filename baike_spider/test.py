import requests
from bs4 import BeautifulSoup
url = "http://baike.baidu.com/item/Python"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml', from_encoding='utf-8')
print(soup)