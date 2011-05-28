#~ -*-coding:utf-8-*-


def histogram(dizge):
	str = dizge.lower()
	nharf = {}
	for harf in str:
		if harf.isalpha():
			nharf[harf] = nharf.get(harf, 0) + 1
	a = nharf.keys()
	b = nharf.values()
	for i in range(len(a)):
		print a[i], ":", b[i]

#histogram("sefa ali veli selami kara goz kara kas besiktas samsunspor")
