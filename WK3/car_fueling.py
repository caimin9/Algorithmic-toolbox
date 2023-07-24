import sys

def compute_min_refills(distance, tank, stops):
    # Add the starting point (0) and final destination (distance) to the list of stops
    stops = [0] + stops + [distance] 
    
    num_refills = 0 
    curr_position = 0 
    

    while curr_position < len(stops) - 1:
        # Store the position where the car is before it moves
        last_position = curr_position
        
        # Move forward as long as the next stop is reachable without refueling
        while curr_position < len(stops) - 1 and stops[curr_position + 1] - stops[last_position] <= tank:
            curr_position += 1
        
        # If the car didn't move, then the next stop is not reachable, return -1
        if curr_position == last_position:
            return -1
        
        # If the car has not reached the destination, it needs to refuel
        if curr_position < len(stops) - 1:
            num_refills += 1

    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
