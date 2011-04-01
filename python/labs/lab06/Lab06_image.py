import Image
res = Image.open("scarlet.jpg")
print "Tur   :", res.format, "\nBoyut :", res.size, "\nRenk :", res.mode
resim = res.transpose(Image.ROTATE_90)
resim.show()
