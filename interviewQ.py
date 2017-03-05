#!/usr/bin/python

#Print X in a matrix form

def matrixprinting(n) :
   "This function prints a sq matrix form with X as diagonal elements"   
   k = n-1   
   for i in range(0,n): 
      for j in range(0,n):      
         if ((i == j) or (j == k)) :
            print 'x' + ' ',
         else: 
            print '_' + ' ',
      k = k-1
      print '\n'
   return

def count_digits(n):
   "This function counts number of digits in n"
   count = 0
   print ("number of digits ="),len(str(n))
   x = n     
   while (x != 0):
     x = n%10
     n = n/10
     if (x): 
       count = count + 1     
   print 'Number of digits =', count
   return count
   
n = 4
matrixprinting(n)

m = 123
print count_digits(m)
exit