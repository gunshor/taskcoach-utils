from icalendar import Calendar, Event
from datetime import datetime
from icalendar import UTC # timezone

import xml.etree.ElementTree as ET
tree = ET.parse('Tasks.tsk')
root = tree.getroot()

#1
#print root.tag
#print root.attrib

#2
#for task in root:
#    #print task.tag
#    if task.tag == 'task':
#        for child in task:
#            if child.tag == 'effort':
#                print child.attrib

#3
#for task in root.findall('task'):
#    for effort in task.findall('effort'):
#        start = effort.get('start')
#        stop = effort.get('start')
#        print 'Start: ' + start + ' Stop: ' + stop
        
#    for subtask in task.findall('task'):
#        for effort in task.findall('effort'):
#            start = effort.get('start')
#            stop = effort.get('start')
#            print 'Start: ' + start + ' Stop: ' + stop

def createCalendar():
    cal = Calendar()
    cal.add('prodid', 'Task Coach Util //')
    cal.add('version', '2.0')

    return cal

def saveCalendar():
    f = open('example.ics', 'wb')
    f.write(calendar.as_string())
    f.close()
    

def createICSEvent(subject, id, priority, start, stop):
    event = Event()
    event.add('summary', subject)
    event.add('dtstart', datetime.strptime(start, '%Y-%m-%d %H:%M:%S'))
    event.add('dtend', datetime.strptime(stop, '%Y-%m-%d %H:%M:%S'))
    #event.add('dtstamp', datetime. (2005,4,4,0,10,0,tzinfo=UTC))
    event['uid'] = id
    event.add('priority', priority)
    calendar.add_component(event)

    
def iterateTasks(root):
    for child in root:
        if child.tag == 'task':
            iterateTasks(child)
        elif child.tag == 'effort':
            subject = root.get('subject')
            #priority = root.get('priority')
            start = child.get('start')
            stop = child.get('start')
            id = child.get('id')
            createICSEvent(subject, id, 0, start, stop)
            print 'Task: ' + subject + ' Start: ' + start + ' Stop: ' + stop



calendar = createCalendar();
iterateTasks(root);
saveCalendar();
