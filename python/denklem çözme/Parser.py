import re
from lib2to3.tests.support import parse_string

def parse_string(str=None):
    """\
    Do very, very primitive parsing of a string into a plist.
    'x' is the only term considered for the polynomial, and this
    routine can only handle terms of the form:
    7x^2 + 6x - 5
    and will choke on seemingly simple forms such as
    x^2*7 - 1
    or
    x**2 - 1
    """
    termpat = re.compile('([-+]?\s*\d*\.?\d*)(x?\^?\d?)')
    #print "Parsing string: ",str
    #print termpat.findall(str)
    res_dict = {}
    for n,p in termpat.findall(str):
        n,p = n.strip(),p.strip()
        if not n and not p: continue
        n,p = parse_n(n),parse_p(p)
        if res_dict.has_key(p): res_dict[p] += n
        else: res_dict[p] = n
    highest_order = max(res_dict.keys())
    res = [0]*(highest_order+1)
    for key,value in res_dict.items(): res[key] = value
    return res


def parse_n(str):
    "Parse the number part of a polynomial string term"
    if not str: return 1
    elif str == '-': return -1
    elif str == '+': return 1
    return eval(str)
 
def parse_p(str):
    "Parse the power part of a polynomial string term"
    pat = re.compile('x\^?(\d)?')
    if not str: return 0
    res = pat.findall(str)[0]
    if not res: return 1
    return int(res)