import os

os.listdir()
os.path.join(dirname, filename)
os.path.abspath(path) #returns a complete path
os.path.exists(pathanme)
os.mkdir(dirname)

import shutil
shutil.copy(source, destiny) #copies a file for you!

import commands
cmd = 'ls -l' + dirname
(status, output) = commands.getstatusoutput(cmd)
if status:
	sys.stderr.write('there was an error:' + output)
	sys.exit(1)
print output 