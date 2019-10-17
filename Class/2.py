a_dict = {'a':[1,2,4,5,6], 'text':'text'}

print(a_dict)

print(a_dict['a'])

a_dict['newkey']='key'


print(a_dict)

a_dict['key'] = [1,24,5,6,7]

print(a_dict['key'][1])

print(type(a_dict['key']))

type(None)
type(True)
type(False)
type(False,)
a=None
b=False

if a == b:
	print(a)
else:
	print(a)
	print(b)

if bool(a) == b:
	print(a)
else:
	print(a)
	print(b)

inp = input("Enter data: ")

print(type(inp))

a_tuple={1,2,3,'text'}
try:
	a_tuple.append('new')
except:
	pass

a_list = [1,2,3,45,67,0]
try:
	a_list.append('z')
	print(a_list)
except:
	pass


def test(a,b,c):
	res = str(a) + str(b) + str(c)
	return res

print(test(a, b, 6))