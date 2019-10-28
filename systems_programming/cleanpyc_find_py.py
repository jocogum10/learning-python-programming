"""
find and delete all "*.pyc" bytecode files at and below the directory
named on the command-line; this uses a python-coded find utility, and
so is portable; run this delete .pyc's from an old python release;
"""

import os, sys, find            # here, gets tools.find

count = 0
for filename in find.find('*.pyc', sys.argv[1]):
    count += 1
    print(filename)

print('Removed %d .pyc files' % count)