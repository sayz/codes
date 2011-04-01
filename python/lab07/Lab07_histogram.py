#~ -*-coding:utf-8-*-
#dizgilerin karakter histogramını çıkaran program
def histogram(str):
	nharf = {}
	for harf in str:
		nharf[harf] = nharf.get(harf, 0) + 1
	a = nharf.keys()
	b = nharf.values()
	for i in range(len(a)):
		print a[i], ":", b[i]

#örnek kullanım:
histogram('sekiz yuz seksen sekiz')
