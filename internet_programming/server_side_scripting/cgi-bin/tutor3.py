"""
runs on the server, reads from input, prints HTML;
url=http://server-name/cgi_bin/tutor3.py
"""
import cgi
form = cgi.FieldStorage()           # parse form data
print("Content-type: text/html")    # plus blank line

html = """
<TITLE> tutor3.py </TITLE>
<H1>Greetings</H1>
<HR>
<P>%s</P>
<P>%s</P>
<HR>
"""
if not 'user' in form:
    print(html % ('Who are you?', form))
else:
    print(html % ('Hello, %s' % form['user'].value, form))