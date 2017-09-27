# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:06:57 2017

@author: raveendra.seetharam
"""

#!/usr/bin/python

import time
import datetime
import Doctor
#from Doctor import *

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
    self.generatePatientId() 
    self.DocId = 0

 def generatePatientId(self):
     self.patientId = self.telnum
     
 def getMaxPatientCount(self):
    count = 0
    for p in PatientList:
        count += 1
    return count

 def DisplayPatientDetails(self):
    for p in PatientList:
        print ("Name :", p.firstname, p.lastname)
        print ("profession :", p.profession)
        print ("Disease :", p.disease)
        print ("PatientId :", p.patientId)
            
        age = calculate_age(p.birthdate)
        print ("Age =",age)
            
        if (p.deceased == 1):
            print ("Patient deceased")
        else:
            print ("Patient Alive")     

def AssignPatientToDoctor(TelNum):
    #Assign based on the disease.
    exists = 0
    for p in PatientList:
         if(p.telnum == TelNum):
            exists = 1           
            if (p.disease == "Fever"):
                print ("Assign Physician")
                for d in DoctorList:
                    if(d.specilization == "Physician"):
                        p.DocId = d.DoctorId
                    else:
                        print("Keep looking")
            elif(p.disease == "Heart"):
                print ("Assign Cardio")
            elif(p.disease == "Brain"):
                print ("Assign Nuero")
            else:
                print ("Cannot determine")      
    
    if(exists == 0):
        print ("Patient Doesnt Exist")
    
    
def calculate_age(birthdate):
     birthyear = birthdate.split(',')
     currentyear = datetime.datetime.today().date()
     #print ("birthyear,currentyear",int(birthyear[0]),currentyear.year)
     age = currentyear.year - int(birthyear[0])
     return age
    
def SearchPatientDetails(TelNum):
    exists = 0
    for p in PatientList:
         if(p.telnum == TelNum):
            exists = 1
            print ("Name :", p.firstname, p.lastname)
            print ("profession :", p.profession)
            print ("Disease :", p.disease)
            print ("PatientId :", p.patientId)
            print ("Assigned Doc:",p.DocId)
            
            age = calculate_age(p.birthdate)
            print ("Age =",age)
            
            if (p.deceased == 1):
                print ("Patient deceased")
            else:
                print ("Patient Alive")
         
    if(exists == 0):
        print ("Patient Doesnt Exist")
 
def DeletePatientDetails(TelNum):
    exists = 0
    for p in PatientList:
         if(p.telnum == TelNum):
            exists = 1
            print ("deleting Patient :", p.firstname, p.lastname , "information")
            PatientList.remove(p)
         
    if(exists == 0):
        print ("Patient Doesnt Exist")           

if __name__ == "__main__":
  PatientList = []
  patient = Patient("Raj","kundra","PA","1234","Fever","0","1975,7,23")
  PatientList.append(patient)
  patient1 = Patient("Ravi","Ram","CEO","1235","cold","0","1984,3,12")
  PatientList.append(patient1)
  print (PatientList)
  count = patient.getMaxPatientCount()
  print ("Num of Patients=",count)
  
  patient.DisplayPatientDetails()
  
  AssignPatientToDoctor("1234")
  
  print("After Assigning Doc")
  SearchPatientDetails("1234")
  
  print("\nSearch for non-existent patient")
  SearchPatientDetails("1236")
  
  print ("\nDelete Patient Record")
  DeletePatientDetails("1234")
  
  count = patient.getMaxPatientCount()
  print ("\nNum of Patients=",count)
  patient.DisplayPatientDetails()
