# Shitty script to generate graphs
# for multiple sizes at once.

# Should be self descriptive.
BITS_MIN=8
BITS_MAX=20	# Inclusive.

ROUNDING="rtz"

for i in $(seq $BITS_MIN 1 $BITS_MAX)
do
	python check.py $i $ROUNDING knbit.csv
	echo "${i}ks-${i}bs-${i}as k, a, b combination for base n = ${i}" > config.txt
	python grapher.py knbit.csv config.txt
	mv *.png graphs
done
