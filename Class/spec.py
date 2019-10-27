import sys

def is_icecream_sandwich(str):
	is_yes = False
	for i in range(int(len(str)/2)):
		if len(str) < 3:
			return False
		if str[i] != str[-i-1]:
			return False
		if str[i + 1] != str[i] and not is_yes:
			is_yes = True
		elif str[i + 1] != str[i] and is_yes:
			return False
	return is_yes

print(is_icecream_sandwich(sys.argv[1]))