

year = int(input("请输入年份:"))

def isLeapYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

print("{0}{1}是闰年".format(year,('' if isLeapYear(year) else '不')))