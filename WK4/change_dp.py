#What we're gonna end up doing is building up a table to keep track of the min num of coins needed for each amount from 1 to m (our total money)
#We're only dealing with 1c, 3c & 4c coins
import sys

def get_change(m):
    #Only working with 1c , 3c, 4c
    coins = [1,3,4]
    #Initialise a list to record how much coins are needed to make change for each value 1 to m
    #Multiply by m to make the list a size of m+1
    min_num_coins = [0] + [float('inf')] * m
    
    #For each money we need to calculate the min no. of coins needed to make that amount. We go through each amount from 1 to the total change m
    #So if m is 27c we go from 1c, 2c, 3c, ...., 27c
    for money in range(1,m+1):
        for i in coins:
            #i here is either 1,3 or 4, So we are going through each value
            if money >= i:
                # money - i is the remaining amount
                #here I'm saying the number of coins needed are the min num of coins needed for the previous value + 1
                num_coins = min_num_coins[money - i] +1
                #This is checking for a better solution for the current value we are trying to find the minimum number of coins to give back as change
                if num_coins < min_num_coins[money]:
                    min_num_coins[money] = num_coins
    return min_num_coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
