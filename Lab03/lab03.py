import requests, sys, re, threading
from bs4 import BeautifulSoup


class KarnavalParse():

    def __init__(self):
        try:
            self.avg_price = int(sys.argv[2])
            self.list_urls = []
            self.list_near_product = {}
            for i in range(int(sys.argv[1])):
                self.list_urls.append(f'https://prom.ua/ua/Karnavalnye-kostyumy-iuzhskie;{i + 1}')
            self.user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36' }
        except ValueError:
            print("Incorrect arguments")
            sys.exit()
        except IndexError:
            print("Need more arguments")
            sys.exit()
        except:
            print("Incorrect URL")
            sys.exit()

    def get_all_data(self):
        self.list_products = {}
        for url in self.list_urls:
            r = requests.get(url, headers = self.user_agent)
            t = threading.Thread(target=self.__get_data, args=(r, ))
            t.start()
            t.join()

    def __get_data(self, req):
        print(".", end = '')
        soup = BeautifulSoup(req.text, features='html.parser')
        div_products = soup.find_all('div', {'class':'x-gallery-tile__content'})
        for prod in div_products:
            soup = BeautifulSoup(str(prod), features='html.parser')
            if soup.find('span', {'class':'x-gallery-tile__price'}) is not None:
                self.list_products.update({ soup.find('a', {'data-qaid':'product_name'}).get_text(): soup.find('span', {'class':'x-gallery-tile__price'}).get_text().rstrip().lstrip('\n')})

    def get_near_two_products(self):
        iterator = iter(self.list_products.items())

        min_above_product = next(iterator)
        min_below_product = min_above_product
        price = float(re.findall(r'[-+]?([0-9]*\,[0-9]+|[0-9]+)', min_above_product[1].replace('\xa0', ''))[0].replace(',', '.'))
        df = self.avg_price - price
        if df <= 0:
            min_above_diff = abs(self.avg_price - price)
            min_below_diff = 999999999999999999999999999
        else:
            min_above_diff = 999999999999999999999999999
            min_below_diff = abs(self.avg_price - price)
        try:
            while True:
                product = next(iterator)
                price_cur = float(re.findall(r'[-+]?([0-9]*\,[0-9]+|[0-9]+)', product[1].replace('\xa0', ''))[0].replace(',', '.'))
                diff = self.avg_price - price_cur
                if diff <= 0 and abs(diff) < min_above_diff:
                    min_above_diff = abs(diff)
                    min_above_product = product
                elif diff > 0 and abs(diff) < min_below_diff:
                    min_below_diff = abs(diff)
                    min_below_product = product
        except StopIteration:
            if min_above_diff != 999999999999999999999999999 and min_below_diff != 999999999999999999999999999:
                self.list_near_product.update(dict([[min_above_product[0], min_above_product[1]], [min_below_product[0], min_below_product[1]]]))
            else:
                self.list_near_product.update(dict([[min_above_product[0], min_above_product[1]]]))
            return


    def show_filter_data(self):
        print('\n---------------------------------------')
        for name, price in self.list_near_product.items():
            print(name + "\nPrice: " + price, end = '\n---------------------------------------\n')

    def show_all_data(self):
        for name, price in self.list_products.items():
            print(name + "\nPrice: " + price, end = '\n---------------------------------------\n')

    def parse(self):
        self.get_all_data()
        self.get_near_two_products()
        self.show_filter_data()

karnaval_parse = KarnavalParse()
karnaval_parse.parse()

