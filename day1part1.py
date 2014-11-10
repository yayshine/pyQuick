#!/usr/bin/python2.7.5 -tt
# Copyright 2014 Yayshine. All Rights Reserved.

import sys

def Hello(name):
	if name == 'Yay' or name == 'Yayshin':
		print 'Oh my god you are here!'
		name = name + ' the awesome'
	else:
		print 'Else'
		DoesNotExist(name)
	name = name + '!!!!!!!'
	print 'Hello', name # when , is used to add things, you get a space b/w them

# Define a main() function that prints a little greeting.
def main():
	Hello(sys.argv[1])


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()



#in python interpreter
#import moduleName
#dir(moduleName) ==> shows all the symbols that's defined insisde
#help(moduleName) ==> explanation on the features

#***Python only checks the line when it is run

#strings are immutable in Python

#string slices work in negative numbs
#last letter is -1 (imagine it's -1 from the len)