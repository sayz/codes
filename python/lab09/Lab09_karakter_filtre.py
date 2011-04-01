def filtre(fp,st):
	fl = open(fp)
	for i in fl:
		if st not in i:
			print i.strip()
			
filtre("sozcuk.txt","j")
