from bs4 import BeautifulSoup
import requests 

url = 'https://www.detmir.ru/catalog/index/name/kolyaski/page/2/'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html_parser')


