#We're given a number of items with weights and values corresponding to each one. We have a bag that can only store a certain amount of weight
#We need to maximise this value given our weight conditions

import sys
#This function finds the most valuable item we per weight from the items given to us

def BestItem(w,v):
    max_val_pw = 0
    best_item = 0
    
    for i in range(len(w)):
        if w[i] > 0:
            val_pw = v[i]/w[i]
            if val_pw > max_val_pw:
                max_val_pw = val_pw
                best_item = i
    return best_item
    


def get_optimal_value(capacity, weights, values):
  
    
    total_value= 0                  #initialising a variable to store the total value already stored in the bag
    for index in range(len(weights)):            #Gonna loop through the total number of values we have from [0:n]
        if capacity == 0:           #Check to see if there's any space left in the bag
            return(total_value)     #if not return the total value of the items we have in the bag 
        index = BestItem(weights,values)
        a = min(weights[index],capacity)   #We let a variable called a equal to the smallest of either weight or capacity
        total_value = total_value +a*(values[index]/weights[index])   #We now let the total value equal to the amount already stored in the bag  + 
                                                            #the smaller of (weights or capacity) x (vals/weights)
        weights[index] = weights[index] - a     #We reduce the value of weights since it's been added to the knapsack      
        capacity = capacity - a
    return(total_value)
    
#Problem is it's exceeding the toatl amount able to hold in the bag




if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
