#-*-coding:utf-8-*-
import csv, random

#dosya açılıp, varlığı denetleniyor:
def dosyaAc():
	try:
		wordlist = csv.reader(open("wordlist.csv", "rb"))
		return wordlist
	except:
		print "böyle bir dosya yok: wordlist.csv"
wordlist = dosyaAc()

#dosyadaki kelimeleri sözlüğe gönderiyoruz:
def putinto():
	sozluk = {}
	for words in wordlist:
		sozluk[words[0]] = words[1][1:]
	return sozluk

#ingilizce kelimelerden rastgele bir kelime alıyoruz:
def randomKelime(liste):
	randWord = random.choice(liste)
	return randWord

#küme yöntemi ile kelimeler arasındaki harf farkları tespit ediliyor:
def farkListesi(str1, str2):
	farkListe = []
	for fark in set(str1) - set(str2):
		farkListe.append(fark)
	return farkListe

#hata yüzdesi hesaplanıyor:
def yuzdeBul(elem1, elem2):
	return ((len(elem1) * 100) / len(elem2))

#uzunluk farklarının mutlak değeri:
def uzAbs(key, value):
	return abs(len(key) - len(value))

#hatalar denetleniyor:
def hataDenetle(hatayuz, cevap):
	if  100 >= hatayuz >= 50:
		print "çok fazla hata var düzelt!!!, hata oranı: % s" %hatayuz
	elif 50 > hatayuz > 5:
		print "biraz hata var, hata oranı: %s" %hatayuz
	elif  uzAbs(trsi,sozluk[randWord])> 2:
		print "kelimelerin uzunlukları çok farklı"
	else:
		print "tebrikler cevabınız doğru, gerçek cevap: %s" %cevap

#şimdi fonksiyonlarımızı çağırıyoruz.
#sozluk = putinto()

#randWord = randomKelime(sozluk.keys())

#trsi = raw_input("%s: türkçesi nedir?\n" %(randWord))

#farkL = farkListesi(trsi, sozluk[randWord])

#yuzde = yuzdeBul(farkL, sozluk[randWord])

#hataDenetle(yuzde, sozluk[randWord])
