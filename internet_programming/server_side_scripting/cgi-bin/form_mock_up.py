"""
Tools for simulating the result of a cgi.FieldStorage()
call; useful for testing CGI scripts outside the Web
"""

class FieldMockup:              # mocked-up input object
    def __init__(self, str):
        self.value = str
        
def form_mock_up(**kwargs):     # pass field = value args
    mockup = {}                 # multichoice: [value,...]
    for (key, value) in kwargs.items():
        if type(value) != list:
            mockup[key] = FieldMockup(str(value))
        else:
            mockup[key] = []
            for pick in value:
                mockup[key].append(FieldMockup(pick))
    return mockup
    
def selftest():
    # use this form if fields can be hardcoded
    form = form_mock_up(name='Bob', job='hacker', food=['Spam', 'eggs', 'ham'])
    print(form['name'].value)
    print(form['job'].value)
    for item in form['food']:
        print(item.value, end=' ')
    # use real dict if keys are in variables or computed
    print()
    form = {'name': FieldMockup('Brian'), 'age': FieldMockup(38)}   # or dict()
    for key in form.keys():
        print(form[key].value)
        
if __name__ == '__main__':
    selftest()