"""
A python script to download and play a media file by FTP.
Uses getfile.py, a utility module which encapsulates FTP step.
"""

import getfile
from getpass import getpass
filename = 'monkeys.jpg'

# fetch with utility
getfile.getfile(file=filename, site='ftp.rmi.net', dir='.', user=('lutz', getpass('Pswd?')), refetch=True)

# rest is the same
if input('Open file?') in ['Y', 'y']:
    from systems_programming.Media import playfile
    playfile(filename)