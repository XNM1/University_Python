import json
from urllib.request import urlopen
import sys

class JSONParse():
	
	def __init__(self):
		try:
			self.url = urlopen("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
		except:
			sys.exit()
	
	def print_json(self):
		print(self.url)
		currency = json.load(self.url)
		#print(currency)
		print('''
		
		
		
		
		
		
		''')
		
		if len(currency) > 0:
			matrix = []
			for i in range(len(currency)):
				matrix.append((list(currency[i].values())))
			print(matrix)
			map = []
			for cur in matrix:
				map.append({"r": cur[0], "text": cur[1], "rt": cur[2], "c":cur[3], "date":cur[4]})
			print(json.dumps(map))
			
		
jsonparse = JSONParse()
jsonparse.print_json()