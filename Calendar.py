#Hello World
#!/usr/bin/python

from clock import clock

class Calendar:
  month = (31,28,31,30,31,30,31,31,30,31,30,31)

  def __init__(self):
    self.day = 0
    self.month = 0
    self.year = 0

  def set(self,day,month,year):
    self.day = day
    self.month = month
    self.year = year

  def IsLeapYear(self,year):
    #x = self.year % 4
    if (year % 4):
      # Not Leap Year
      return 0
    else:
      # Leap Year
      if (year % 100):
        return 1
      else:
        if (year % 400)
          return 0
        else:
          return 1

  def Countdays(self,day,month,year):
    "This method counts days on a 24 hours basis"
       
    #Get max days in the month from 
    Max_days = month[self.month-1)]
        
    if(Max_days == self.day):
      self.day = 1
      if (self.month == 12):
        self.month = 1
        self.year += 1
      else:
        self.month += 1
    else:
      #Count for 24 hours and increment day
      #TODO :: Here call the counthour method from clock class.
      self.day += 1   

  def get ()
    return (self,self.day,self.month,self.year)