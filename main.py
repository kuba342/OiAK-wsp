
from math import floor, ceil, log2


XPlus = {
	'rtz': lambda d, n: d + n # Jakieś wyrażenie zamiast 'd + n' 
}

XMinus = {}
YPlus = {}
YMinus = {}


def findK(d, x, sign):
	k = 0
	while True:
		exp = 2**k / ((sign * 2**k) % d)
		if exp > x:
			return k
		
		k += 1


def findKPlus(d, n, scheme: str):
	return findK(d, XPlus[scheme](d, n), -1)
	

def findKMinus(d, n, scheme: str):
	return findK(d, XMinus[scheme](d, n), 1)


def findAPlus(k, d):
	a = ceil(2**k / d)
	assert a > 0

	return a


def findAMinus(k, d):
	a = floor(2**k / d)
	assert a > 0
	
	return a

	
def minh(a, b):
	p = floor(max(log2(a), log2(b)))	# Get position of the most significant bit.
	mask = 2**p							# We'll use a mask to get to each bit.
	c = 0
	while (mask > 0):
		if ((a & mask) == (b & mask)):
			c |= (a & mask) 			# Set bit in c if the same is set in a (and b for that matter).
			a &= ~mask		 			# Clear this bit in a.
		else:
			c += 2**ceil(log2(a))
			break
		
		mask >>= 1;
	
	return c;
	

def findB(y):
	b = minh(*y)
	assert b >= 0
	
	return b
	
	
def findBPlus(k, a, d, n, scheme: str):
	return findB(YPlus[scheme](k, a, d, n))
	
	
def findBMinus(k, a, d, n, scheme: str):
	return findB(YMinus[scheme](k, a, d, n))
	

def findKab(d, n, scheme):
	kPlus = findKPlus(d, n, scheme)
	kMinus = findKMinus(d, n, scheme)
	
	assert kPlus >= 0
	assert kMinus >= 0
	
	if kPlus < kMinus:
		a = findAPlus(kPlus, d)
		b = findBPlus(kPlus, a, d, n, scheme)
		
		return kPlus, a, b
	else:
		a = findAMinus(kMinus, d)
		b = findBMinus(kMinus, a, d, n, scheme)
		
		return kMinus, a, b
		
	
def div(x, k, a, b, n):
	return floor((a * x + b) / 2 ** k) % 2**n


def main():
	x = 44
	d = 11
	n = 6
	
	# Parsing arguments and sewch.
	#print(findKab(11, 6, 'rtz'))
	print(div(x, 8, 23, 16, n), floor(x / d))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Yooooo, eyyy.