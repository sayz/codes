import doctest
def faktoriyeL(n):
	"""\
		>>> faktoriyeL(9)
		362880
		>>> faktoriyeL(4)
		24
		>>> faktoriyeL(1)
		1
		>>> faktoriyeL(0)
		1
		>>> faktoriyeL(-8)
		Negatif tamsayilarin faktoriyel hesaplamasi yapilamaz.
	"""
	if n == 0 or n == 1:
		return 1
	elif n < 0:
		print "Negatif tamsayilarin faktoriyel hesaplamasi yapilamaz."
	else:
		return n * faktoriyeL(n-1)
doctest.testmod()
