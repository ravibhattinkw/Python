# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:01:49 2017

@author: raveendra.seetharam
"""

class Doctor:
    "Base class for all Doctors in the hospital"
    
    def __init__(self,FirstName,LastName,Specilization,TelNum):
        self.firstname = FirstName
        self.secondname = LastName
        self.specilization = Specilization
        self.telnum = TelNum
        self.generateDoctorId()       
    
    def generateDoctorId(self):
        self.DoctorId = self.telnum
    
    def getDoctorId(self):
        return self.DoctorId

if __name__ == "__main__":
  DoctorList = []
  doctor = Doctor("R","B","Physician","0234")
  DoctorList.append(doctor)
  doctor1 = Doctor("R","Re","Cardio","0235")
  DoctorList.append(doctor1)
  print (DoctorList)