from event import Event
import datetime
from yamldriver import  *


day = str(datetime.date.today())
desc = 'This is a test event'
event = Event(day,'Testvent',desc)

#event.report()
event.addTask('Task', 'This is a test task')
#event.tasks[0].report()
write_yaml('./test2.yml',event)
#print(event.calcPercent())

