#!/usr/bin/python

#daily_balances = [107.92, 108.67, 109.86, 110.15]
#  "slice starting 3 days ago: [108.67, 109.86]"
#  "slice starting 2 days ago: [109.86, 110.15]"

def display_balances(n,daily_balances):
    listlen = 0
    for b in daily_balances:
        listlen += 1
    print listlen
    startingIndex = listlen - n
    print startingIndex
    
    if (startingIndex >= 0):
    	balance = []
    	balance.append(daily_balances[startingIndex])
    	balance.append(daily_balances[startingIndex+1])
    	print ("dailyBalance = ",balance)
    else:
    	print ("Given slice is beyond list len")
    
    
    
if __name__ == "__main__":
     
     daily_balances = [107.92, 108.67, 109.86, 110.15]
     slice = 6
     display_balances(slice,daily_balances)