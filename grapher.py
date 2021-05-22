import matplotlib.pyplot as plt
import numpy as np
import sys

'''
	O1 - 1
	ln - log n
	On - n
	nl - n log n
	n2 - n^2
	n3 - n^3
	...
	
'''

# If True, won't generate plots.
had_error = False

def error(*args):
	print(*args)
	had_error = True
	

class Plot:
	def __init__(self, xs, ys, legend, xlabel, ylabel, title, styles):
		self.xs = xs
		self.ys = ys
		self.legend = legend
		
		# These do not change after merge.
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.title = title		# Maybe do make a custom title as an argument?
		
		self.styles = styles
		
		self.can_merge = True	# Label that it is an actual plot.

	def make_plot(self):
		# Sets the state.
		plt.title(self.title)
		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)
		
		for x, y, style in zip(self.xs, self.ys, self.styles):
			plt.plot(x, y, style)
		
		plt.legend(self.legend, loc=2)		# Legend in upper left corner.
		
	
	def merge(self, p: 'Plot') -> 'Plot':
		if not p.can_merge:
			error('Attempting to merge a plot that is a generic big O boi.')
			return None
			
			
		return Plot(self.xs + p.xs, self.ys + p.ys, self.legend + p.legend, p.xlabel, p.ylabel, p.title, self.styles + p.styles)	
		
	
class BigO(Plot):
	def __init__(self, f, legend):
		self.f = f			# Modifier? Lambda? Big OOOoooOO? Whatever...
		self.legend = legend
		self.can_merge = False
	
	def merge(self, p: Plot) -> Plot:
		if not p.can_merge:
			error('Attempting to merge a plot that is a generic big O boi.')
			return None
		
		# Find max x and its value.
		cor_x = p.xs[0][-1]
		max_y = max(p.ys[0])
		min_y = min(p.ys[0])
		for x, y in zip(p.xs, p.ys):
			if max(y) > max_y:
				cor_x, max_y = x[-1], max(y)
			
			min_y = min(min(y), min_y)
			
		
		print(cor_x, max_y)
		
		x = np.linspace(1, cor_x)
		y = min_y + (self.f(x)*(max_y - min_y))/self.f(x[-1])
		
		return Plot(p.xs + [x], p.ys + [y], p.legend + [self.legend], p.xlabel, p.ylabel, p.title, p.styles + [''])
	
plots = {}

def pseudoplots():
	plots['O1'] = BigO(lambda x : x/x, 'O(1)')
	plots['ln'] = BigO(lambda x : np.log(x), 'O(log(n))')
	plots['nl'] = BigO(lambda x : x * np.log(x), 'O(nlog(n))')
	plots['n2'] = BigO(lambda x : x ** 2, 'O(n^2)')
	

def add_plot(config, xs, ys):
	# Basic config check.
	if len(config) < 4:
		print('Invalid config:', config)
		exit(1)
	
	# Config.
	id = config[0]
	title = config[1]
	xlabel = config[2]
	ylabel = config[3]
	legend = config[4]
	
	
	xInts, yInts = [int(x) for x in xs], [int(y) for y in ys]
	
	plot = Plot([xInts], [yInts], [legend], xlabel, ylabel, title, ['--o'])	# Make a new plot.
	plots[id] = plot														# Add plot.


sep = ','

def read_data(s: str):
	with open(s, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		
		# Eh.
		i = 0
		while i < len(lines):
			# IMPLICIT ASSUMPTION - data always starts at 
			#  first line AND is correct.
			add_plot(lines[i].split(sep), lines[i+1].split(sep), lines[i+2].split(sep))
			i += 3
			
			# Skip empty lines.
			while i < len(lines) and (not lines[i] or lines[i].isspace()):
				i += 1


def combine(combs):
	for comb, title in combs:
		split = comb.split('-')
		
		plot = plots[split[0]]
		for id in split[1:]:
			plot = plots[id].merge(plot)

		plot.title = title
			
		print(comb)
		plots[comb] = plot
	

def get_combinations(filename):
	combs = []
	with open(filename, 'r') as f:
		for line in f:
			id = line.split()[0]
			name = line[len(id):].strip()
			
			combs.append((id, name))

	return combs
	
	
def save():
	for id, plot in plots.items():
		if not plot.can_merge:
			continue
	
		plot.make_plot()
		plt.savefig(id + '.png')
		plt.clf()


def main():
	if len(sys.argv) < 2:
		usage()
		exit(1)
	
	# Retrieve source filename.
	filename = sys.argv[1]
	
	# Retrieve combinations.
	combinations = get_combinations(sys.argv[2]) if len(sys.argv) >= 3 else []
	print(combinations)
	
	# Initialize 'pseudo-plots'
	pseudoplots()
	
	# Load data for plotting.
	read_data(filename)
	
	# Make plot combinations.
	combine(combinations)
	
	# Save generated plots.
	save()

main()