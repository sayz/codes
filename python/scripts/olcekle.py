#!/usr/bin/python
#-*-coding:utf-8-*-
import Image
import sys
import os

detail = False


def vers():
	return "olcekle1.0"


def yardim():
	help_text = """
	kullanmadan önce:
		chmod +x olcekle.py

	komutlar:
		-h --- bu metni görüntüler
		-v --- ayrıntılı gösterir
		-s --- sürüm gösterir

	kullanım:
		./olcekle.py [file ..]

	örnekler:
		$./olcekle.py $(ls images/*)

		$./olcekle.py image.jpg
		"""
	return help_text


def olcekle(images, dir):
	i = 1
	while i < len(images):
		image = images[i]
		ext = os.path.splitext(image)[1]
		base = os.path.basename(os.path.splitext(image)[0])
		basename = base + ext
		try:
			im1 = Image.open(image)
			width = im1.size[0]
			height = im1.size[1]
			im2 = im1.resize((width / 4, height / 4))
			if detail:
				print basename + " işleniyor..."
				im2.save(dir + "/" + base + "-o" + ext.lower())
				print "işlendi"
			else:
				im2.save(dir + "/" + base + "-o" + ext.lower())
		except IOError:
			if detail:
				print "verilen -->" + basename + "<-- dosyası bir resim dosyası değil!!!"
			else:
				pass
		i = i + 1


def main():
	global detail
	default_dir = "resizes"
	images = sys.argv
	if len(sys.argv) == 1:
		print  "yardım için ----> $./olcekle.py -h"
		exit(0)
	if sys.argv[1] == "-v":
		detail = True
		images = sys.argv[1:]
	if sys.argv[1] == "-h":
		print yardim()
	elif sys.argv[1] == "-s":
		print vers()
	else:
		try:
			os.mkdir("./" + default_dir)
			olcekle(images, default_dir)
		except OSError:
			evha = raw_input(default_dir + " dizini zaten var, ölçeklenen dosyalar bu dizine kaydedilsin mi(E/h)?")
			if evha == "E" or evha == "e" or evha == "":
				olcekle(images, default_dir)
			elif evha == "H" or evha == "h":
				nondef_dir = raw_input("istediğiniz dizinin adını giriniz>")
				olcekle(images, nondef_dir)


if __name__ == '__main__':
	main()