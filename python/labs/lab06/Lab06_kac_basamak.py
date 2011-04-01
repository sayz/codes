import doctest
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
		return 1
	else:
		while n:
			sayac += 1
			n = abs(n) / 10
		return sayac	
