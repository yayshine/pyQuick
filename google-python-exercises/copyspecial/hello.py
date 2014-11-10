import commands
import sys
import os

def List(dir):
	cmd = 'ls -l ' + dir
	print 'about to do this: ', cmd
	return
	(status, output) = commands.getstatusoutput(cmd)
	#if status:
	#	print sys.stderr 'there was an error: ', output
	#	sys.exit(1)
	print output

def main():
	List(sys.argv[0])

if __name__ == '__main__':
	main()