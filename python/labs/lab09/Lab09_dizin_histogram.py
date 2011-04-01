#~ -*-coding:utf-8-*-
from os import walk,path,getcwd

pat = raw_input("içerik histogramını istediğiniz dizinin yolunu\
 '/.../dizin' şeklinde giriniz:\n")
kok_dizin = pat
ndiz, ndos = 0, 0
print walk(kok_dizin)

#~ bütün alt klasörlerdeki dosyalar dahil taramaya başlıyoruz. 
for yol,dizinler,dosyalar in walk(kok_dizin):
	ndiz += 1
	for dosya in dosyalar:
		ndos += 1
print "Klasor Sayısı:", ndiz
print "Dosya Sayısı:", ndos
