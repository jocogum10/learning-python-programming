"""
show hello world syntax for input language name; note that it uses r'...'
raw strings so that '\n' in the table are left intact, and cgi.escape()
on the string so that things like '<<' don't confuse browsers--they are
translated to valid HTML code; any language name can arrive at this script,
since explicit URLs "http://servername/cgi-bin/languages.py?language=Cobol"
can be typed in a web browser or sent by a script (urllib.request.urlopen).
caveats: the languages list appears in both the CGI and HTML files--could
import from single file if selection list generated by a CGI script too;
"""
debugme = False             # True=test from cmd line
inputkey = 'language'

hellos = {
    'Python':       r" print('Hello World')                 ",
    'Python2':      r" print 'Hello World'                  ",
    'Perl':         r' print "Hello World\n";               ',
    'Tcl':          r' puts "Hello World"                   ',
    'Scheme':       r' (display "Hello World") (newline)    ',
    'SmallTalk':    r" 'Hello World' print.                 ",
    'Java':         r' System.out.println("Hello World");   ',
    'C':            r' printf("Hello World\n");             ',
    'C++':          r' cout << "Hello World" << endl;       ',
    'Basic':        r' 10 PRINT "Hello World"               ',
    'Fortran':      r" print *, 'Hello World'               ",
    'Pascal':       r" WriteLn('Hello World');              ",
}

class dummy:                    # mocked-up input obj
    def __init__(self, str):
        self.value = str
        
import cgi, sys
if debugme:
    form = {inputkey: dummy(sys.argv[1])}       # name on cmd line
else:
    form = cgi.FieldStorage()                   # parse real inputs

print('Content-type: text/html\n')              # adds blank line
print('<TITLE>Languages</TITLE>')
print('<H1>Syntax</H1><HR>')

def showHello(form):                            # HTML for one language
    choice = form[inputkey].value
    print('<H3>%s</H3><P><PRE>' % choice)
    try:
        print(cgi.escape(hellos[choice]))
    except KeyError:
        print("Sorry--I don't know that language")
    print('</PRE></P><BR>')

if not inputkey in form or form[inputkey].value == 'All':
    for lang in hellos.keys():
        mock = {inputkey: dummy(lang)}
        showHello(mock)
else:
    showHello(form)
print('<HR>')