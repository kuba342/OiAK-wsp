from check import save
from main import findKab

import sys


def optimalNForK(n, scheme):
	d = 2**(n-1) - 1
	print(d)
	k, _, _ = findKab(d, n, scheme)
	return k
	
def kForN(minN, maxN, scheme):
	nks = {}
	for n in range(minN, maxN + 1):
		nks[n] = optimalNForK(n, scheme)
	
	return nks


def main():
	nks = kForN(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
	print(nks)
	
	# Transform for writing to file.
	ns, ks = [], []
	for n, k in nks.items():
		ns.append(n)
		ks.append(k)
		
	with open(sys.argv[4], 'w', encoding='utf-8') as f:
		save(f, 'nk,Najmniejsze k, które pasuje dla wszystkich d.,n,k,k', ns, ks)
	
	

if __name__ == '__main__':
    main()