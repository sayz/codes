def yarilar_toplam(n):
	a = 0
	for i in range(n):
		n = n / 2.0
		if n <= 0.1:
			break
		else:
			a += n
	return a
		
print yarilar_toplam(7)
