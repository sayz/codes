#-*-coding:utf-8-*-
from math import *
def kok_hesapla(a, b, c):
	delta = b ** 2 - 4 * a * c
	if delta < 0:
		print "Bu denklemin reel kökü hesaplanamaz"
	else:
		w1 = (-b + sqrt(delta)) / 2 * a
		w2 = (-b - sqrt(delta)) / 2 * a
		print "Denklemin 1. kökü: %f" %w1
		print "Denklemin 2. kökü: %f" %w2
a = input("a katsayısını giriniz:")
b = input("b katsayısını giriniz:")
c = input("c katsayısını giriniz:")
kok_hesapla(a, b, c)
