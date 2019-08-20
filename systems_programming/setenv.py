import os
print('setenv...', end=' ')
print(os.environ['USERNAME'])

os.environ['USERNAME'] = 'Joco'
os.system('py echoenv.py')

os.environ['USERNAME'] = 'Carlos'
os.system('py echoenv.py')

os.environ['USERNAME'] = input('?')
print(os.popen('py echoenv.py').read())