import events
import datetime
import  util


day = str(datetime.date.today())
desc = 'This is a test event'
event = Event(day,'Testvent',desc)

#event.report()
event.addTask('Task', 'This is a test task')
#event.tasks[0].report()
write_yaml('./',event)
#print(event.calcPercent())

