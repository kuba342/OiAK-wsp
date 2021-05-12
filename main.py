
from math import floor, ceil, log2


XPlus = {
	'rtz': lambda d, n: d + n # Jakieś wyrażenie zamiast 'd + n' 
}

XMinus = {}
YPlus = {}
YMinus = {}


def findK(d, n, x, sign):
	for k in range(n):
		exp = 2**k / ((sign * 2**k) % d)
		if exp > x:
			return k
		
	raise Exception('Could not find suitable k.')


def findKPlus(d, n, scheme: str):
	return findK(d, n, XPlus[scheme](d, n), -1)
	

def findKMinus(d, n, scheme: str):
	return findK(d, n, XMinus[scheme](d, n), 1)


def findAPlus(k, d):
	return ceil(2**k / d)


def findAMinus(k, d):
	return floor(2**k / d)
	

def findB(y):
	return minh(*y)
	
	
def findBPlus(k, a, d, n, scheme: str):
	return findB(YPlus[scheme](k, a, d, n))
	
	
def findBMinus(k, a, d, n, scheme: str):
	return findB(YMinus[scheme](k, a, d, n))
	

def findAkb(d, n):
	pass


def main():
	# Parsing arguments and sewch.
	print(XPlus['rtz'](1, 2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Yooooo, eyyy.