#-*-coding:utf-8-*-
import kac_basamak
import string

ls = ["spam!", 1, ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]

for i in range(len(ls)):
	if str(ls[i]) in string.digits:
		print i, ":", ls[i], ":", kac_basamak.kac_basamak(ls[i])
	elif ls[i] == list(ls[i]):
		#print ls[i], ":", len(ls[i])
		for j in range(len(ls[i])):
			print i, ":", j, ":", ls[i][j]
	else:
		print i, ":", ls[i], ":", len(ls[i])
