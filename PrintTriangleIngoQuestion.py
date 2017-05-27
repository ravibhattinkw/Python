#!/usr/bin/python

def printTriangle(n):
   pos = (2 * n - 1)/2
   spos = epos = pos
      
   i = 0
   while (i < n):
      j = 0
      while (j <= epos):
          if (j >= spos):
             print 'x' + ' ',
          else:
             print ' ' + ' ',
          j = j+1
      print '\n'
      spos = spos - 1
      epos = epos + 1 
      i = i+1      
   return      

if __name__ == "__main__":
  printTriangle(5)
