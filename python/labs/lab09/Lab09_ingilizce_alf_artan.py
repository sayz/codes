def alfa(str):
	a = list(str)
	b = a[:]
	b.sort()
	if a == b:
		return True
	else:
		return False
fp = open("words.txt","r")
sayac = 0
for satir in fp:
	nsiz = satir.strip()
	if alfa(nsiz):
		print nsiz
		sayac += 1
print " sıralı kelime sayisi:\t" , sayac
