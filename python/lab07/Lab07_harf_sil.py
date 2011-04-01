#-*-coding:utf-8-*-
def hsil(h,str):
	arinmis = ""
	for i in range(len(str)):
		if h != str[i]:
			arinmis += str[i]
	return arinmis

#örnek kullanım:
hsil("s","mississdsipi")
#çıktı:
#miidipi
