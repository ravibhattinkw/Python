#!/usr/bin/python
#This program Walks through the repository and extracts all the available files
#It prints the path to the file
#count the number of files
#time take to search the repository

import os, time

t = time.time()
n = 0

for root,dirs,files in os.walk("./"):
  for file in files:
    n += 1
t = time.time() - t
print "os.walk: took %s seconds,%d files found" % (t,n) 
for file in files:
  path = os.path.join(root,file)
  print "path =", path