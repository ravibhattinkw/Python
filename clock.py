#!/usr/bin/python
import time

class Clock:
  "A Test class for General clock"
  
  def __init__(self):
    "Constructor"
    self.sec = 0
    self.min = 0
    self.hour = 0
    
  def set (self,hour,min,sec):
    "This will initialize Hour,min and Sec to user value"
    self.sec = sec
    self.min = min
    self.hour = hour
  
  def Tick (self,hour,min,sec):
    "This method will count by one second"
    if (self.sec == 59):
      self.sec = 0
      if (self.min == 59):
        self.min = 0
        self.hour += 1
        if (self.hour == 23):
          self.hour = 0
      else:
        self.min += 1
    else:
      self.sec += 1
      
  def display(self):
    "This method will display time"
    i = 0
    while (i<10000):
      time.sleep(1)
      self.Tick(self.hour,self.min,self.sec)
      print ("%d:%d:%d" % (self.hour, self.min, self.sec))
      i += 1
  
  def __str__(self):
    return "%2d:%2d:%2d" % (self.hours,self.min,self.sec)
      

if __name__ == "__main__":
  ClockObj = Clock()
  ClockObj.set(8,35,0)
  ClockObj.display()

