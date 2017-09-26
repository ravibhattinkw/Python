#!/usr/bin/python

import time
import datetime

class Patient:
 "A Patient Record Class"

 
 #def __init__(self,FirstName,LastName,TelNum,birthdate,disease,deceased):
 def __init__(self,FirstName,profession,LastName):
    "Constructor"
    self.firstname = FirstName
    self.profession = profession
    self.lastname = LastName
    #self.birthdate = birthdate
    #self.disease = disease
    #self.deceased = deceased
    #self.telnum = TelNum
    #self.time = time()
    self.patientId = patientId
    self.patientId += 1
    
    
 def displayPatient(self,PatientId):   
     if (PatientDict['PatientId'] == PatientId):
        print ("Name :", PatientDict['name'])
        #print ("Age  :", PatientDict['age'])
        #print ("disease :",PatientDict['disease'])


#def enrolPatient(FirstName,LastName,TelNum,birthdate,disease,deceased):
#    for i=0 in range(5):
#        Patientlist.append({Patient(FirstName,LastName,TelNum,birthdate,disease,deceased)})

patientId = 1
#Patientlist = [dict() for x in range(5)]
#patient = Patient("Raj")
#print(patient.firstname)
#Patientlist.append({patient})
#print Patientlist
people = [Patient("Nick", "Programmer","carter"), Patient("Alice","Engineer","johnson")]
Patientlist = dict([ (p.firstname, p.profession, p.lastname) for p in people ])
print Patientlist