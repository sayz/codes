def yoL_secici(x, y, z):
    a = int(not(x) and not(y) and z)
    b = int(not(x) and y and not(z))
    c = int(not(x) and y and z)
    d = int(x and not(y) and not(z))
    e = int(x and not(y) and z)
    f = int(x and y and not(z))
    g = int(x and y and z)
    print "a : %d\nb : %d\nc : %d\nd : %d"%(a,b,c,d)
    print "e : %d\nf : %d\ng : %d" %(e,f,g)
yoL_secici(0, 0, 0)
print "==========="
yoL_secici(0, 0, 1)
print "==========="
yoL_secici(0, 1, 0)
print "==========="
yoL_secici(0, 1, 1)
print "==========="
yoL_secici(1, 0, 0)
print "==========="
yoL_secici(1, 0, 1)
print "==========="
yoL_secici(1, 1, 0)
print "==========="
yoL_secici(1, 1, 1)
