#~ -*-coding:utf-8-*-
def analiz(l):
	ks,ts,os,bs,ls = 0,0,0,0,0
	for i in l:
		if type(i) == int:
			ts +=1
		elif type(i) == float:
			os +=1
		elif type(i) == bool:
			bs +=1
		elif type(i) == str:
			ks +=1
		else:
			ls +=1
	print "karakter:%d\ntamsayı:%d\nondaliksa\
yı:%d\nbool:%d\nliste:%d\n" %(ks,ts,os,bs,ls)

#örnek kullanım:
analiz([1, '1.1', [1.1, 1.1], [False, 7, True], -1])
