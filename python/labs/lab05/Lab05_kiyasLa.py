def kiyasla(s1, s2):
	"""
	  >>>kiyasla(9, 4)
	  1
	  >>>kiyasla(3, 13)
	  -1
	  >>>kiyasla(6, 6)
	  0
	"""
	if s1 > s2:
		return 1
	elif s2 > s1:
		return -1
	else:
		return 0
