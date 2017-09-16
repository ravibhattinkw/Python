#!/usr/bin/python
import time


def SearchString(filename,str):
   count = 0
   t = time.time()
   FileHandle = open(filename, 'r')
   for line in FileHandle:
      if str in line:
        count += 1
   t = time.time() - t 
   print "Found %d times in %f seconds" % (count,t)

filename = 'Out.rtf'
str = "Blackberry"
SearchString(filename,str)