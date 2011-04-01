#~ -*-coding:utf-8-*-
def alfa(str):
	a = list(str)
	b = a[:]
	b.sort()
	if a == b:
		return True
	else:
		return False

alfa("adem")
