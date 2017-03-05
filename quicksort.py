#!/usr/bin/python

#QuickSort using Recursion
def Partition(sortarray,start,end):
    "This function works as per Partition logic"
    pivot = sortarray[end]
    pindex = start    
    if (start < end):
        for i in range (start,end):            
	        if (sortarray[i] <= pivot):
	            sortarray[i],sortarray[pindex] = sortarray[pindex],sortarray[i]
	            pindex +=1	
        sortarray[pindex],sortarray[end] = sortarray[end],sortarray[pindex]
    return pindex
           
def quicksort(sortarray,start,end):
    "This function executes QuickSort recurssively"
    if (start < end):
        pindex = Partition(sortarray,start,end)
        quicksort(sortarray,start,pindex-1)
        quicksort(sortarray,pindex+1,end)
    return
        
sortarray = [3,7,28,5,22,6,98,5,14,12,0,2]
start = 0
end = len(sortarray)
print 'length=',end
quicksort(sortarray,start,end-1)
print "sorted array is", sortarray