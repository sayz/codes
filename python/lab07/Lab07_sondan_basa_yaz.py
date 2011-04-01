#-*-coding:utf-8-*-
import string
def sondan_basa_yaz(cumle):
	nsen = ""
	if cumle != str(cumle):
		print "karakter gir"
	else:
		for i in range(1,len(cumle)+1):
			nsen += cumle[-i]
		print nsen
sondan_basa_yaz("idelkecreg zidliy afes udok ub")
