# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:06:57 2017

@author: raveendra.seetharam
"""

#!/usr/bin/python

import time
import datetime

patientId = 1

class Patient:
 "Base Patient Record Class"
 
 def __init__(self,FirstName,LastName,profession,TelNum,Disease,Deceased,Birthdate):
    "Constructor for creating patient record"
    self.firstname = FirstName
    self.lastname = LastName
    self.profession = profession
    self.telnum = TelNum
    self.disease = Disease
    self.deceased = Deceased
    self.birthdate = Birthdate
    self.patientId = patientId
    self.patientId += 1

 def getMaxPatientCount(self):
    return self.patientId
 
def calculate_age(birthdate):
     birthyear = birthdate.split(',')
     currentyear = datetime.datetime.today().date()
     #print ("birthyear,currentyear",int(birthyear[0]),currentyear.year)
     age = currentyear.year - int(birthyear[0])
     return age
    
def displayPatientDetails(TelNum):
     for p in PatientList:
         if(p.telnum == TelNum):
            print ("Name :", p.firstname, p.lastname)
            print ("profession :", p.profession)
            print ("Disease :", p.disease)
          
            age = calculate_age(p.birthdate)
            print ("Age =",age)
            
            if (p.deceased == 1):
                print ("Patient deceased")
            else:
                print ("Patient Alive")
            

if __name__ == "__main__":
  PatientList = []
  patient = Patient("Raj","kundra","PA","1234","Fever","0","1975,7,23")
  PatientList.append(patient)

  patient1 = Patient("Ravi","Ram","CEO","1235","cold","0","1984,3,12")
  PatientList.append(patient1)
  print (PatientList)
  count = patient.getMaxPatientCount()
  print ("Num of Patients=",count)
  
  displayPatientDetails("1235")
