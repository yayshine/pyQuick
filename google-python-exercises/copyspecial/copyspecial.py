#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

"""List special file(='\w*__\w+__\w*')'s absolute paths"""
def listSpeFiles(dirName):
  speFileList = []
  filenames = os.listdir(dirName)
  for filename in filenames:
    if re.search(r'__\w+__', filename):
      speFileList.append(os.path.abspath(os.path.join(dirName, filename)))
  return speFileList

def storeSpeFiles(filenames, destination):
  if not os.path.exists(destination):
    os.mkdir(destination)
    for filename in filenames:
      shutil.copy(filename, destination)
  else:
    print "Destination folder already exists!"

def compressSpeFiles(filenames, zipName):
  cmd = 'zip -j ' + zipName
  for filename in filenames:
    cmd += ' ' + filename
    (status, output) = commands.getstatusoutput(cmd)
  if status:
    print "Something went wrong with compressing"
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  speFileList = []
  for dirName in args:
    speFileList.extend(listSpeFiles(dirName))

  if todir:
    storeSpeFiles(speFileList, todir)

  if tozip:
    compressSpeFiles(speFileList, tozip)
  
if __name__ == "__main__":
  main()
