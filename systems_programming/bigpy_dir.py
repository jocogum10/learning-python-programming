"""
find the largest python source file in a single directory.
search windows python source lib, unless dir command-line arg.
"""

import os, glob, sys
dirname = r'C:\Users\cgumanay\AppData\Local\Programs\Python\Python37\Lib' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))
    
allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])