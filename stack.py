# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:06:57 2017
@author: raveendra.seetharam
"""

#!/usr/bin/python

class Stack:
     #"Base class for stack implementation"
     
    def __init__(self):
         self.items = []
         
    def push(self, number):
         self.items.append(number)
        
    def pop(self):
         if self.isEmpty():
            print ("Empty Stack")
         else:
            return self.items.pop()
    
    def isEmpty(self): 
        if(len(self.items) == 0): 
             return 1
        else:
             return 0

if __name__ == '__main__':
    s = Stack()
    s.push (1)
    s.push (5)
    s.push (8)
    print s.items
    ret = s.pop()
    print ret
    print s.items
    name = "Raveendra"
    
    for i in range (0,len(name)):
        s.push(name[i])
    print s.items
    
    reverse = []
    print("Pop from stack")
    for i in range (0,len(name)):
        ret_val = s.pop()
        reverse.append(ret_val)
    print ('reverse=' ,reverse)

             
