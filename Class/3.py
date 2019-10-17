import sys

class FirstClass:
	def __init__(self):
		self.a = 1
		self.b = 2

	def summ(self, a):
		self.a = self.b + 3
		res = int(self.a) * int(a)
		return res

	def arvchecker(self, check, b):
		if check == 'Start':
			return self.summ(b)
try:
	class_object = FirstClass()
	print(class_object.arvchecker(sys.argv[2], sys.argv[1]))
except:
	sys.exit()
