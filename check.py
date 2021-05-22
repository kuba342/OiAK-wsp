from main import findKab, testRange, test

from sys import argv

sep = ','

def allD(n, ds, scheme):
	ks, a_s, bs = [], [], []
	for d in ds:
		k, a, b = findKab(d, n, scheme)
		
		"""
		Note: disabled for bulk graph generation.
		invalid = testRange(k, a, b, test[scheme], n, d)
		if len(invalid) != 0:
			print(f'Error! With k={k}, a={a}, b={b}, incorrect values for x in {invalid}')
		"""
		
		ks.append(k)
		a_s.append(a)
		bs.append(b)
		
	return ks, a_s, bs
	

def save(f, header, xs, ys):
	f.write(header + '\n')
	f.write(sep.join(map(str, xs)) + '\n')
	f.write(sep.join(map(str, ys)) + '\n')
	

def generate(n, scheme, filename):
	
	# Generate odd ds between 3 and 2^m.
	ds = [d for d in range(3, 2**n) if d % 2 == 1]
	
	# Get all ks, as, bs.
	ks, a_s, bs = allD(n, ds, scheme)
	
	# Save em.
	with open(filename, 'w', encoding='utf-8') as f:
		save(f, f'{n}ks,"Optymalne" k dla kolejnych wartosci d,d,k,k', ds, ks)
		save(f, f'{n}as,"Optymalne" a dla kolejnych wartosci d,d,a,a', ds, a_s)
		save(f, f'{n}bs,"Optymalne" b dla kolejnych wartosci d,d,b,b', ds, bs)
		
	
def main():
	if len(argv) != 1 + 3:
		print('Usage: n rounding_scheme output_file')
		return 1
		
	generate(int(argv[1]), argv[2], argv[3])
	

main()