#Class which recieves information to describe an event.
# name and desc should be strings
# date should be datime object
from task import Task

class Event():
  
  def __init__(self, date, name, desc='', start=0, end=0):
    self.date = date
    self.name = name
    self.desc = desc
    self.tasks = []
    self.startTime = start
    self.endTime = end
    
  def listTasks(self):
    for item in self.tasks:
      print(self.tasks[item])

  def report(self):
    print (self.name)
    print (self.date)
    print(self.desc)
 
  def addTask(self,tname,tdesc):
    x = Task(tname,tdesc)
    self.tasks.append(x)
    
  def calcPercent(self):
    total = len(self.tasks)
    completed = 0
    
    
    for item in self.tasks:
      if item:
        completed += 1
      else:
        completed += 0
        
    percent = float(completed) / float(total) 
    
    percent = percent * 100
    
    return percent
      
        
    
    
  
    
   
    
    
    
    
  

