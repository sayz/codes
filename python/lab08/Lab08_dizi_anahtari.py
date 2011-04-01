#~ -*-coding:utf-8-*-
def dizi_anahtari(diz):
	strlist = diz.split("-")
	intlist = []
	top = 0
	for i in strlist:
		intlist.append(int(i))
		top += int(i)
	ort = top / len(intlist)
	a = ort
	intlist.sort()
	uz = len(intlist)
	if uz % 2 != 0:
		b = intlist[uz / 2]
	else:
		b = (intlist[uz / 2] + intlist[uz / 2 - 1]) / 2
	key = a * b
	return key
	
#kullanımı:	
dizi_anahtari('3-5-7-10')
dizi_anahtari('3-10-7-5')
dizi_anahtari('3-10-7')
