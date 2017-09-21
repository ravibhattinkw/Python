#!/usr/bin/python

# Take max numbers to generate as input 
# Generate sequence as 0 1 1 2 3 5 8 13 21 34 
# For example if input n = 5 then generate 0 1 1 2 3
from __future__ import print_function

def GenerateNumber (n):
   SecondPrev = 0
   FirstPrev = 1
   print ("The Sequence is %d %d"%(SecondPrev,FirstPrev), end=' ')
   
   for i in range (0,n-2):
      nextNum = FirstPrev + SecondPrev
      SecondPrev = FirstPrev
      FirstPrev = nextNum
      print (nextNum, end =' ')
 
GenerateNumber(8)