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

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    """Get a dir name and returns a list of the
       special names in the list
    """

    filenames = os.listdir(dir)
    special_names = []

    for filename in filenames:

        if re.search(r'__(\w+)__', filename):
            path = os.path.abspath(filename)
            special_names.append(path)

    return special_names


def copy_to(paths, dir):
    """ Copy the files in paths to dir, if dir does't exists
        creates it
    """

    # If not dir creates it
    if not os.path.exists(dir):
        os.mkdir(os.path.abspath(dir))

    # Copy files to dir
    for path in paths:
        to_dir =  os.path.abspath(dir)
        shutil.copy(path, dir)

def zip_to(paths, zippath):
    """

    :param paths:
    :param zippath:
    :return: given a list of paths, zip those files up into the given zipfile
    """

    files = ""

    for path in paths:
        files += path + " "

    command = "zip -j %s %s" % (zippath, files)

    print "Command I'm going to do:" + command

    (status, output) = commands.getstatusoutput(command)

    if status:
        print status, "\n", output


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

  # +++your code here+++
  # Call your functions

  filenames = []

  for arg in args:
      names = get_special_paths(arg)
      for name in names:
          print name
      filenames += names
      if todir:
          copy_to(names, todir)
      if tozip:
          zip_to(names, tozip)


if __name__ == "__main__":
  main()
