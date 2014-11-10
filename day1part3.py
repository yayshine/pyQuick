import sys

# dictionary/hashtable
d = {}
d['a']='alpha'
d['o']='omega'
d['g']='gamma'

d.keys()
d.values()
d.items()

# file
def Cat(filename):
	f = open(filename, 'rU')
	for line in f:
		print line, #added comma adds things without a line break

	# OR
	lines = f.readlines()
	
	# OR
	text = f.read()

	f.close()

def main():
	Cat(sys.argv[1])

if __name__ == '__main__':
	main()