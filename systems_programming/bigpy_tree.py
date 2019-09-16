"""
find the largest python source file in an entire directory tree.
search the python source lib, use pprint to display results nicely.
"""

import sys, os, pprint
trace = True
if sys.platform.startswith('win'):
    dirname = r'C:\Users\cgumanay\AppData\Local\Programs\Python\Python37\Lib'
else:
    dirname = '/usr/lib/python'     # Unix, Linux, Cygwin
    
allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))
            
allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
