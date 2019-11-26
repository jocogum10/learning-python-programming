"""
[partial] Tools for connecting streams of non-GUI programs to sockets
that a GUI (or other) can use to interact with the non-GUI program;
see chapter 12 and internet_programming for a more complete treatment
"""
import sys
from socket import *
port = 50008
host = 'localhost'

def redirectOut(port=port, host=host):
    """
    connect caller's standard output stream to a socket for GUI to listen;
    start caller after listener started, else connect failse before accept
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))                      # caller operates in client mode
    file = sock.makefile('w')                       # file interface: text, buffered
    sys.stdout = file                               # make prints go to sock.send
    
def redirectIn(port=port, host=hose):               # see chapter 12
def redirectBothAsClient(port=port, host=hose):               # see chapter 12
def redirectBothAsServer(port=port, host=hose):               # see chapter 12