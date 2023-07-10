#Want to create a greedy algorithm to minimise the total amount of coins needed to give back the given change 'm'
#from a list of 1c, 5c, & 10c coins

import sys

def get_change(m):
    list = [1,5,10]                          #types of change are 1c, 5c, & 10c
    i = 0
    while m > 0:                             #m is the total change
        a = max(list)                        #take the coin with the greatest value from the list
        if a > m:
            list.remove(a)                   #get rid of the coins that are more than the change needed
        else:
            m = m-a                          #total change needed to return has now decreased by the value of the coin we extracted from the list
            i +=1                            #Increment count by 1
    return i                                 #Return the count of how many coins we had to use
    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
