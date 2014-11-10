#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys, re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # opens file and reads it
  f = open(filename, 'rU')
  text = f.read()

  # get the year
  year = re.search('Popularity in (\d+)', text)
  year = year.group(1)


  # gets the names and rank
  tuples = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  # creates the dict to have exactly one name per rank
  babyDict = {}
  for babytuple in tuples:
    (rank, boyname, girlname) = babytuple
    if babyDict.get(girlname) and babyDict[girlname] < rank: pass
    else: babyDict[girlname] = rank
    if babyDict.get(boyname) and babyDict[boyname] < rank: pass
    else: babyDict[boyname] = rank

  # creates the list of year, name and rank
  babyList = [year]
  for key in babyDict.keys():
    babyList.append(key+' '+babyDict[key])
  babyList = sorted(babyList)

  return babyList


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  while len(args):
    namesList = extract_names(args[0])  
    text = '\n'.join(namesList)
    if summary:
      f = open(args[0]+'.summary', 'w')
      f.write(text)
    else:
      print text
    del args[0]

if __name__ == '__main__':
  main()
