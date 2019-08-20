"""
split and interactively page a string, file, or stream of
text to stdout; when run as a script, page stdin or file
whose name is passed on cmdline; if input is stdin, can't
use it for user reply--use platform-specific tools or GUI;
"""
import sys

def getreply():
    """
    read a reply key from an interactive user
    even if stdin redirected to a file or pipe
    """
    if sys.stdin.isatty():                      #if stdin is console
        return input('?')                       # read reply line from stdin
    else:
        if sys.platform[:3] == 'win':           #if stdin was redirected
            import msvcrt                       #can't use to ask a user
            msvcrt.putch(b'?')
            key = msvcrt.getche()               #use windows console tools
            msvcrt.putch(b'\n')                 #getch() does not echo key
            return key
        else:
            assert False, 'platform not supported'

def more(text, numlines=10):
    """
    page multiline string to stdout
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and getreply() not in [b'y', b'Y']: break
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())