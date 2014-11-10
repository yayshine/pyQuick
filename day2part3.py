import sys
import urllib

uf = urllib.urlopen('http://google.com')
uf.read()
urllib.urlretrieve('http://google.com/images/srpr/logo9w.png', 'blah.png')


def Cat(filename):
	try:
		f = open(filename)
		text = f.read()
		print '---', filename
		print text
	except IOError:
		print "****************************"
		print filename, 'doesn\'t exist!'
		print "****************************"

def main():
	args = sys.argv[1:]
	for arg in args:
		Cat(arg)

if __name__ == '__main__':
	main()