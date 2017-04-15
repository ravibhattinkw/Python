#!/usr/bin/python
#This code counts occurance of subsequent letters
#aaabbbcc will be printed as a3b3c2

def countchar(str):  
  i=1
  count = 1
  j = 0
  #print str
  #print "len=",len(str)
  FinalString = []
  c = str[j]
  while ( i < len(str)) :
    #print "i and c and next c", i,str[j],str[j+1]
    if str[j] == str[j+1]:
      count += 1
      c = str[j]
    else:
      FinalString.append(c)
      FinalString.append(count)
      #initialize the counter back to 1
      count = 1
      #print FinalString 
    i += 1
    j += 1
  FinalString.append(c)
  FinalString.append(count)
  print FinalString
  return;

if __name__ == "__main__":
  mystring = 'aabbcc'
  countchar(mystring)