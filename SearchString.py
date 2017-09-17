#!/usr/bin/python
import time


def SearchString(filename,str):
   count = 0
   lines = []
   t = time.time()
   FileHandle = open(filename, 'r')
   for line in FileHandle:
      if str in line:
        lines.append(line)
        count += 1
   t = time.time() - t 
   print ("Found %d times in %f seconds" % (count,t))
   return lines,count

filename = 'Out.rtf'
str = 'Blackberry'
lines,count = SearchString(filename,str)
print ("after SearchString count=",count)
for i in range(0,count):
    print ("lines = \n",lines[i])
