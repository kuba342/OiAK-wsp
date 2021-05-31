# Shitty script for bruteforcing without losing progress.

# Should be self descriptive.
BITS_MIN=25
BITS_MAX=40

ROUNDING="rtz"

for i in $(seq $BITS_MIN 1 $BITS_MAX)
do
	python brute.py $i $i "nks-${i}.csv"
done
