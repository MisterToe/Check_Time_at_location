import datetime
import pytz

#Calling specific timezone and formatting output for comparison
PST = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('%H:%M:%S')#Simple hour: minute: seconds string
if PST <= ('09:00:00') or PST >= ('17:00:00'):
    print 'The Portland office is currently closed.'
else:
    print 'The Portland office is currently open.'
print 'Local time: ', PST, '\n'

print '*\n' * 2 #Added breaks to make the output more readable.

EST = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime('%H:%M:%S')
if EST <= ('09:00:00') or EST >= ('17:00:00'):
    print 'The New York office is currently closed.'
else:
    print 'The New York office is currently open.'
print 'Local time: ', EST, '\n'

print '*\n' * 2 #Added breaks to make the output more readable.

BST = datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%H:%M:%S')
if BST <= ('09:00:00') or BST >= ('17:00:00'):
    print 'The London office is currently closed.'
else:
    print 'The London office is currently open.'
print 'Local time: ', BST

