#-*-coding:utf-8-*-
#verilen uzun bir dizgeyi yine verilen kısa dizgeden arındıran program
def arindir(kisa, uzun):
	if kisa in uzun:
		for i in range(len(uzun)):
			if uzun[i:i+len(kisa)] == kisa[:]:
				yenuz = uzun[:i] + uzun[i+len(kisa):]
				return arindir(kisa,yenuz)
	else:
		return uzun


#2. çözümde şu şekilde olabilir:

def arindir(k,u):
	a = u.split(k)
	b = ""
	for i in a:
		b +=i
	return b
