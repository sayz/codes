#~ -*-coding:utf-8-*-
def tc(n):
	a = str(n)
	if len(a) == 11:
		if type(n) == int:
			if n > 0:
				x,y,z = 0,0,0
				for i in range(0,len(a)-2,2):
					x +=int(a[i])
				for j in range(1,len(a)-2,2):
					y +=int(a[j]) 
				if (7*x-y) % 10 == int(a[9]):
					print "geçerli TC nosu"
				else:
					print "geçerli TC nosu degil" 
			else:
				print "Lütfen 11 haneli bir tamsayı giriniz"
		else:
			print "Lütfen 11 haneli bir tamsayı giriniz"
	else:
		print "Lütfen 11 haneli bir tamsayı giriniz"
#örnek kullanım:
tc(42250767586)
