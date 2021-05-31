from main import testBasic, test, findKab
from check import save

import sys

'''
	Przyjmuję, że a < 2^k,
	bo dla b = 0 -> (x * 2^k)/2^k = x, 
	czyli dzielenie przez 1.

'''
def findA_B(n, d, rounding, k) -> (int, int):
	kRange = 2**k
	
	for a in range(kRange):
		for b in range(a):
			if testBasic(k, a, b, rounding, n, d):
				return (a, b)
				
	return None
	
	
def checkDs(n, k, rounding):
	for d in range(3, 2**n, 2):
		if findA_B(n, d, rounding, k) is None:
			return False
		
	return True
	


def bruteK(n, prevK, scheme):
	upper = 2*n
	rounding = test[scheme]
	
	
	for k in range(prevK, upper):
		if checkDs(n, k, rounding):
			return k
			
	raise RuntimeError('No k to rule them all.')
	

def bruteAll(minN, maxN, scheme):
	nks = {}
	prevK = 9								# Temporarily set to 9.
	for n in range(minN, maxN + 1):
		nks[n] = bruteK(n, prevK, scheme)
		prevK = nks[n]
		
	return nks
	

def main():
	nks = bruteAll(int(sys.argv[1]), int(sys.argv[2]), 'rtz')
	print(nks)
	
	# Transform for writing to file.
	ns, ks = [], []
	for n, k in nks.items():
		ns.append(n)
		ks.append(k)
		
	with open(sys.argv[3], 'w', encoding='utf-8') as f:
		save(f, 'nk,Najmniejsze k, które pasuje dla wszystkich d.,n,k,k', ns, ks)
	
	

if __name__ == '__main__':
    main()