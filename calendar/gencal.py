#class that creates a calendar file for the program to reference when making new events
import calendar 
from os import path

if  path.exists('calrecord'):
  print('yes')
else:
  print('no')

