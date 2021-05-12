import math

def rtz_Xplus(d, n):
    result = d * math.floor((2**n)/d) - 1
    return result

def fr_Xplus(d, n):
    result = math.floor((2**n)/d)
    return result

def rte_Xplus(d,n):
    result = d * math.floor((2**(n+1) - d - 1)/(2*d)) - 1
    return result

def rtz_Xminus(d,n):
    result = d* math.floor((2**n)/d) - d + 1
    return result

def fr_Xminus(d,n):
    result = math.floor((2 ** n) / d)
    return result

def rte_Xminus(d,n):
    result = d * math.floor((2**(n+1) - d - 3)/(2*d)) + 1
    return result

def rtz_Yplus():
    return (0,0)
def rtz_Yminus(k,a,d,n):
    result_1 = ( (2**k - a*d) * math.floor((2**n)/d) )
    result_2 = (2**k - a*(d-1) - 1)
    return result_1, result_2

def fr_Yplus():
    return (0,0)
def fr_Yminus(k,a,d,n):
    result_1 = (2**k - a*d) * math.floor((2**n)/d)
    result_2 = (2**k) - 1
    return result_1, result_2

def rte_Yplus(k,a,d,n):
    # Sprawdzić tą funkcję
    result_1 = int((a*(d-1))/2 + (2**k - a*d))
    result_2 = int((a*(d-1))/2 + (2**k - a*d) * math.floor((2**(n+1) + d - 1)/(2*d)) - 1)
    return result_1, result_2

def rte_Yminus(k,a,d,n):
    result_1 = int( (a*(d-1)/2) + (2**k - a*d) * math.floor( (2**(n+1) + d - 3) / (2*d) ) - 1 )
    result_2 = int( (a*(d+1))/2 + 2**k - a*d - 1 )
    return result_1, result_2
