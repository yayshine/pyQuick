a = [1,2,3]

for num in a:
	print num

# checks if the val is in the list
21 in a

# sorts a list
sorted(a)

sorted(a, reverse=True, key=len) #key=Last etc.

# 2d-custom sorting
def twoDCus(s):
	return ((len(s), s[-1])) #return a tuple

sorted(a, key=twoDCus)

# deletes the variable definition
del a

# concatenates everything in one str
':'.join(a)
# OR
'\n'.join(a)

b = ':'.join(a)
b.split(':')

range(20)

# strings and tuples are IMMUTABLE in PYTHON
# lists are MUTABLE

# assignment
(x, y) = (1, 2)