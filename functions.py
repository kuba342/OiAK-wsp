import math

def rtz_Xplus(d, n):
    result = d * math.floor((2**n)/d) - 1
    return result
    pass

def fr_Xplus(d, n):
    result = math.floor((2**n)/d)
    return result
    pass

def rte_Xplus(d,n):
    result = d * math.floor((2**(n+1) - d - 1)/(2*d)) - 1
    return result
    pass

def rtz_Xminus(d,n):
    result = d* math.floor((2**n)/d) - d + 1
    return result
    pass

def fr_Xminus(d,n):
    result = math.floor((2 ** n) / d)
    return result
    pass

def rte_Xminus(d,n):
    result = d * math.floor((2**(n+1) - d - 3)/(2*d)) + 1
    return result
    pass