'''
Created on 25 Mar 2013

@author: sayz
'''

# -*-coding:utf-8-*-

from Parser import parse_string
from math import log,ceil

def isZero(n):
    if bool(n):
        return n



def bisection(f, lis, x1 = 0, x2 = 1, switch = 1 , tol=1.0e-19):
    
#   f(x1) ve f(x2) eval. 
    
    f1 = f(x1, lis)
    isZero(f1)
    
    f2 = f(x2, lis)
    isZero(f2)
    print "x1: %2.5f, x2: %2.5f " %(x1, x2)
    print "-------------------------------"
    print "f1: %2.5f, f2: %2.5f\n" %(f1, f2)
    # checking f(x1) x f(x2) < 0
    if f1*f2 > 0.0: print 'Root is not bracketed'
    
    #n = ceil(log(abs(x2 - x1)/tol)/log(2.0))
    #print "hata payi %1.10f" %(float((x2 - x1) / (2** (1))))
    
    
    for i in range(6):
        x3 = (x1 + x2) * 0.5
        # f(x3) eval.
        f3 = f(x3, lis)
        #print "hata payi %1.10f" %(float((x3 - x2) / (2** (i+2))))
        if (switch == 1) and (abs(f3) > abs(f1)) \
                         and (abs(f3) > abs(f2)):
            return None
        isZero(f3)
        if f2*f3 < 0.0: x1 = x3; f1 = f3
        else:           x2 = x3; f2 = f3
        print "x1: %2.5f, x2: %2.5f, x3: %2.5f" %(x1, x2, x3)
        print "-------------------------------"
        print "f1: %2.5f, f2: %2.5f, f3: %2.5f\n" %(f1, f2, f3)
    print "="*10
    return (x1 + x2)/2.0

#0.734603507789
#def fx(x, coef_list):
#            result = float(\
#coef_list[len(coef_list)- 1]*x**(len(coef_list)-1) + \
#coef_list[len(coef_list)- 2]*x**(len(coef_list)-2) + \
#coef_list[len(coef_list)- 3]*x**(len(coef_list)-3) +\
#coef_list[len(coef_list)- 4]*x**(len(coef_list)-4))
#            return result
def fx(x, coef_list):
    result = 0
    for j in range(len(coef_list)):
        result += coef_list[len(coef_list)- (j+1)]*x**(len(coef_list)-(j+1))
    return result  
#kat_list = parse_string("x^3 - 10x^2 + 5")
kat_list1 = parse_string("x^2 - 3")
print kat_list1
#print bisection(fx, kat_list, 0.0, 1.0)

print bisection(fx, kat_list1, 1.0, 2.0)
