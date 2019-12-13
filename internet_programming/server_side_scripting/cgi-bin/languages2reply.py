"""
Same, but for easier maintenance, use HTML template strings, get the
Language table and input key from common module file, and get reusable
form field mockup utilities module for testing.
"""

import cgi, sys
from form_mock_up import FieldMockup                # input field simulator
from languages2common import hellos, inputkey       # get common table, name
debugme = False

hdrhtml = """Content-type: text/html\n
<TITLE>Languages</TITLE>
<H1>Syntax</H1><HR>"""

langhtml = """
<H3>%s</H3><P><PRE>
%s
</PRE></P><BR>"""

def show_hello(form):                               # HTML for one language
    choice = form[inputkey].value                   # escape lang name too
    try:
        print(langhtml % (cgi.escape(choice),
                          cgi.escape(hellos[choice])))
    except KeyError:
        print(langhtml % (cgi.escape(choice),
                          "Sorry--I don't know that language"))
                          
def main():
    if debugme:
        form = {inputkey: FieldMockup(sys.argv[1])} # name on cmd line
    else:
        form = cgi.FieldStorage()                   # parse real inputs
        
    print(hdrhtml)
    if not inputkey in form or form[inputkey].value == 'All':
        for lang in hellos.keys():
            mock = {inputkey: FieldMockup(lang)}    # not dict(n=v) here!
            show_hello(mock)
    else:
        show_hello(form)
    print('<HR>')
    
if __name__ == '__main__':
    main()