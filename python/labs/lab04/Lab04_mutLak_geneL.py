# -*-coding:utf-8-*-
def mutlak_genel():
	a = True
	while a:
		islemler ="""\
(1) komplex sayı mutlak değeri
(2) tam sayı mutlak değeri
(3) ondalıklı sayı mutlak değeri
(4) çıkış	
"""
		print islemler
		ans = raw_input("işlem numarasını giriniz:")
		if ans == '1':
			Z_re = input("gerçel kısım:")
			Z_im = input("sanal kısım:")
			mutlak_Z = (Z_re ** 2 + Z_im ** 2) ** 0.5
			print "mutlak değer:", mutlak_Z
		if ans == '2':
			int = input("tamsayı giriniz:")
			print "mutlak değer:", abs(int)
		if ans == '3':
			flo = input("ondalıklı sayı giriniz:")
			print "mutlak değer:", abs(flo)
		if ans == '4':
			a = False
			print "programdan çıktınız!!!"
mutlak_genel()
