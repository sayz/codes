#-*-coding:utf-8-*-
from math import *
def daire_fonk(r):
	if r <= 0:
		print "yarıçap sıfırdan küçük olamaz"
	else:
		cevre = 2 * pi * r
		alan = pi * r ** 2
		print "dairenin çevresi", cevre, "birimdir."
		print "dairenin alanı", alan, "birim karedir."

daire_fonk(4)
