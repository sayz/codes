#!/usr/bin/python
#-*-coding:utf-8-*-


def kac_basamak(n):
	"""
	>>> kac_basamak(67853)
	5
	>>> kac_basamak(600)
	3
	>>> kac_basamak(8)
	1
	>>> kac_basamak(0)
	1
	>>> kac_basamak(-8)
	1
	>>> kac_basamak(-9807)
	4
	"""
	sayac = 0
	if n == 0:
		return sayac + 1
	else:
		while n:
			sayac += 1
			n = n / 10
		return sayac

#print kac_basamak(10)
