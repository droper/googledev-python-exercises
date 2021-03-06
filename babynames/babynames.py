#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

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
import re



def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  ranking = []
  name_list = []
  year_re = '<h3 align="center">Popularity in (\d{4})<\/h3>'
  names_re = '<tr align="right"><td>(\d+)<\/td><td>(\w+)<\/td><td>(\w+)<\/td>'
  file = open(filename, 'r+')

  names = {}

  for line in file:
    year_match = re.search(year_re, line)
    names_match = re.search(names_re, line)
    if year_match:
        ranking.append(year_match.group(1))

    if names_match:
        names[names_match.group(2)] = names_match.group(1)
        names[names_match.group(3)] = names_match.group(1)


  for k, v in names.items():
      name_list.append("%s %s"% (k, v))

  name_list = sorted(name_list)

  #print '\n'.join(ranking + name_list) + '\n'

  return '\n'.join(ranking + name_list) + '\n'


def names_to_file(filenames):
    # Suppose instead of printing the text to standard out, we want
    # to write files containing the text. If the flag --summaryfile is present,
    # do the following: for each input file 'foo.html', instead of printing to
    # standard output, write a new file 'foo.html.summary' that contains the summary
    # text for that file.

    for filename in filenames:

        name = filename + ".summary"

        file = open(name, 'w')
        file.write(extract_names(filename))
        print "Created %s" % filename



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

    names_to_file(args)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  #assert extract_names(args[0])[1]=='Aaliyah 91'

  #extract_names(args[0])

if __name__ == '__main__':
  main()
