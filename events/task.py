#Class  for task objects. Tasks need to have a name , description and a way to
#determine if the task has been completed or not

class Task():
  
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.completed = False
  
  def finish(self):
    self.completed = True
  
  def unfinish(self):
    self.completed = False
    
  def report(self):
    print(self.name)
    print(self.desc)
   
   