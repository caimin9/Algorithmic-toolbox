# points coverered sorted algo
#distance is the distance between destinations
#Tank is the most distance the car can travel at once
#Stops is a list of distances at which the car can refuel

#First off i should compare the stop to the last stop to see if it can go the whole way, if not check the second last one
import sys

#This function just checks that the journey is possible
def check(dist,tnk,stp):
    # Check if the first stop is reachable
    if stp[0] > tnk:
        return -1
    # Check if the destination is reachable from the last stop
    if dist - stp[-1] > tnk:
        return -1
    # Check if each stop is reachable from the previous one
    for i in range(len(stp)-1):
        if stp[i+1] - stp[i] > tnk:
            return -1
    return 0
              


def compute_min_refills(distance, tank, stops):
    #Just check to see if the journey is possible
    if check(distance,tank,stops) == -1: 
        return -1 
    
    #initialise total refills and current position
    refills = 0 
    curr_position = 0
       
    for i in range(len(stops)):
             # If the distance to the next stop is greater than the tank capacity
        if stops[i] > curr_position + tank:
            # If we are at the first stop and can't reach it, return -1
            if i == 0:
                return -1
            # Refill at the current stop and update the current position
            refills += 1
            curr_position = stops[i-1]
            
    
        # Check if we need to refill at the last stop
    if distance > curr_position + tank:
        refills += 1

    return refills
            



if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
