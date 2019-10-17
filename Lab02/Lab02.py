import xml.etree.ElementTree as et
from urllib.request import urlopen
import sys

class XMLParse():

	def __init__(self):
		try:
			self.url = urlopen("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?xml")
		except:
			print('Incorrect URL')
			sys.exit()

	def print_xml(self):
		if len(sys.argv) < 4:
			print("Мінімальна кількість аргументів 3")
			sys.exit()
		tree = et.parse(self.url)
		root = tree.getroot()
		args = list(filter(lambda arg: arg != sys.argv[0], sys.argv))
		result = list(filter(lambda cur: cur.find('cc').text in args, root))
		self.show_currencies(result)

	def show_currencies(self, currencies):
		for cur in currencies:
			print(cur.find('txt').text, end = ": ")
			print(cur.find('rate').text + " грн", end = "; ")
			print("дата: ", end = ": ")
			print(cur.find('exchangedate').text)

xmlparse = XMLParse()
xmlparse.print_xml()