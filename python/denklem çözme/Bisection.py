'''
Created on 22 Mar 2013

@author: sayz
'''
# -*-coding:utf-8-*-

from math import log,ceil

def bisection(f, lis, x1 = 0, x2 = 1, switch = 1 , tol=1.0e-19):
    f1 = f(x1, lis)
    if f1 == 0.0: return x1
    f2 = f(x2, lis)
    if f2 == 0.0: return x2
    if f1*f2 > 0.0: print 'Root is not bracketed'
    n = ceil(log(abs(x2 - x1)/tol)/log(2.0))
    
    for i in range(int(n)):
        x3 = 0.5*(x1 + x2); f3 = f(x3, lis)
        if (switch == 1) and (abs(f3) > abs(f1)) \
                         and (abs(f3) > abs(f2)):
            return None   
        if f3 == 0.0: return x3
        if f2*f3 < 0.0: x1 = x3; f1 = f3
        else:           x2 = x3; f2 = f3
    return (x1 + x2)/2.0