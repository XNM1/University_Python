import requests
from bs4 import BeautifulSoup
import re

url = 'https://prom.ua/ua/Noutbuki'
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
r = requests.get(url, headers = user_agent)
with open('test.html', 'w', encoding='utf-8') as output_file:
	output_file.write(str(r.text))
	a = str(r.text)
#print(a)
soup = BeautifulSoup(a, features='html.parser')
prices_list = soup.find_all('span', {'class':'x-gallery-tile__price'})
name_list = soup.find_all('a', {'data-qaid':'product_name'})
for name, price in zip(name_list, prices_list):
	print(name.get_text() + "\nЦіна: " + price.get_text())