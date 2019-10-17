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
list_products = {}
soup = BeautifulSoup(r.text, features='html.parser')
div_products = soup.find_all('div', {'class':'x-gallery-tile__content'})
for prod in div_products:
	soup = BeautifulSoup(str(prod), features='html.parser')
	if soup.find('span', {'class':'x-gallery-tile__price'}) is not None:
		list_products.update({ soup.find('a', {'data-qaid':'product_name'}).get_text(): soup.find('span', {'class':'x-gallery-tile__price'}).get_text().rstrip().lstrip('\n')})
for name, price in list_products.items():
	print(name + "\nЦіна: " + price)