def ardisik_toplam(n):
	if n <= 0 or n != int(n):
		return "pozitif tamsayi gir"
	else:
		sum = n * (n + 1) / 2
		return sum
		
def ardisik_toplam_2(n):
	if n <= 0 or n != int(n):
		return "pozitif tamsayi gir"
	else:
		a = 0
		for i in range(1,n+1):
			a = a + i
		return a		
