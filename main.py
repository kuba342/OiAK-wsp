
from math import floor, ceil, log2
import sys

import functions


XPlus = {
	'rtz': functions.rtz_Xplus,
	'rte': functions.rte_Xplus,
	'fr': functions.fr_Xplus
}

XMinus = {
	'rtz': functions.rtz_Xminus,
	'rte': functions.rte_Xminus,
	'fr': functions.fr_Xminus
}

YPlus = {
	'rtz': functions.rtz_Yplus,
	'rte': functions.rte_Yplus,
	'fr': functions.fr_Yplus
}

YMinus = {
	'rtz': functions.rtz_Yminus,
	'rte': functions.rte_Yminus,
	'fr': functions.fr_Yminus
}


def isFr(v, x, d):
	division = x / d
	return floor(division) == v or ceil(division) == v

test = {
	'rtz': lambda v, x, d: v == floor(x / d),
	'rte': isFr,	# Wg. artykułu, to wychodzi na to samo.
	'fr': isFr
}


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
	# I might've accidentally fixed something...
	msA = floor(log2(a)) if a != 0 else 0
	msB = floor(log2(b)) if b != 0 else 0
	p = max(msA, msB)					# Get position of the most significant bit.
	mask = 2**p							# We'll use a mask to get to each bit.
	c = 0
	while (mask > 0):
		if ((a & mask) == (b & mask)):
			c |= (a & mask) 			# Set bit in c if the same is set in a (and b for that matter).
			a &= ~mask		 			# Clear this bit in a.
		else:
			c += 2**ceil(log2(a)) if a != 0 else 0
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
	

def usage():
	print(f'Usage: d n {"(" + " or ".join(XPlus.keys()) + ")"} test?')
	print('Returns: k a b')
	
	
def testRange(k, a, b, test, n, d):
	invalids = []
	for x in range(n):
		if not test(div(x, k, a, b, n), x, d):
			invalids.append(x)
			
	return invalids
	

def testBasic(k, a, b, test, n, d) -> bool:
	for x in range(n):
		if not test(div(x, k, a, b, n), x, d):
			return False
	
	return True


def main():
	if len(sys.argv) < 4 or len(sys.argv) > 5:
		usage()
		exit(1)

	d = int(sys.argv[1])
	n = int(sys.argv[2])
	scheme = sys.argv[3]
	
	# Input checking.
	if scheme not in XPlus.keys():
		usage()
		exit(1)
		
	if d % 2 == 0:
		print('d must be odd.')
		exit(1)
		
		
	k, a, b = findKab(d, n, scheme)
		
	if len(sys.argv) != 5:
		print(f'k={k}, a={a}, b={b}')
		exit(0)
	
	if sys.argv[4] != 'test':
		print('Fourth argument must read \'test\'.')
		exit(0)
		
	invalids = testRange(k, a, b, test[scheme], n, d)
	if len(invalids) > 0:
		print('The result does not match {0} values.'.format(invalids))
		print('The first ones being:', invalids[:30])	# Max number of invalid values shown.
		exit(1)
		
	print('All tests passed!')
			
	
	


if __name__ == '__main__':
    main()
