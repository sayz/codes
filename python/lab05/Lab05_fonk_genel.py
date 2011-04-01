def kiyasla(s1, s2):
	if s1 > s2:
		return 1
	elif s2 > s1:
		return -1
	else:
		return 0
def isaret_kontrol(s1, s2):
	if s1*s2 > 0:
		return 1
	elif s1*s2 < 0:
		return -1
	else:
		return 0
def fonk_genel(fonk, s1, s2):
	return fonk(s1, s2)
