__author__ = 'lookmayank'
from math import sqrt
def answer(area):
    lis = []
    while(area >= 1):
        sqr = sqrt(area)
        if(sqr.is_integer()):
            lis.append(int(area))
        else:
            lis.append(int(sqr)**2)
        area = area - (int(sqr)**2)
    return lis
    
