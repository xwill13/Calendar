from event import Event
import datetime

day = str(datetime.date.today())
desc = 'This is a test event'
event = Event(day,'Testvent',desc)

#event.report()
event.addTask('Task', 'This is a test task')
event.tasks[0].report()
#print(event.calcPercent())

