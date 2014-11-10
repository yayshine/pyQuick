#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def url_sort_key(url):
  name = re.search(r'-(\w*)-(\w*)\.(\w*)', url)
  if name:
    return name.group(2)
  else:
    return url

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""

  # Extracts hostname from logfile name
  hostname = re.search('_(.+)', filename)
  hostname = hostname.group(1)

  # Opens logfile
  logfile = open(filename, 'rU')
  logfile = logfile.read()

  # Looks for all urls from logfile
  urls = re.findall('GET\s(\S*)\s', logfile)
  
  # Get rid of duplicates
  urls = list(set(urls))

  # Finds urls with 'puzzle' in them
  puzzleurls = []
  for url in urls:
    if 'puzzle' in url:
      puzzleurls.append("http://"+hostname+url)

  # Sort them in increasing order
  puzzleurls = sorted(puzzleurls, key=url_sort_key)

  return puzzleurls

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # Creates a destination directory if doesn't exist
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  # Retrieves/stores img from urls to dest_dir
  i = 0
  imghtml = open(dest_dir+'/index.html', 'w')
  content = "<html><body>"
  for url in img_urls:
    name = 'img'+str(i)
    print "Retrieving... "+url
    urllib.urlretrieve(url, dest_dir+'/'+name)
    content += "<img src=\""+name+"\">"
    i += 1
  content += "</body></html>"
  
  imghtml.write(content)
  imghtml.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
