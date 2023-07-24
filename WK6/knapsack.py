
import sys
'''
w is the value of the individual weights
capacity is the total amount of weight capacity in our bag
table with 1,2,...,capacity[-1]
I want my matrix to be of dimensions len(w)+1
'''

def optimal_weight(capacity, weights):
    n = len(weights)
    m = capacity 
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for w in range(1, m+1): # Starts from 1, not weights[i-1]
            if weights[i-1] <= w: # If weight of the current item is less than or equal to the current capacity
                matrix[i][w] = max(matrix[i-1][w], weights[i-1] + matrix[i-1][w-weights[i-1]]) 
            else: # If weight of the current item exceeds the current capacity
                matrix[i][w] = matrix[i-1][w]  # Just take the value of not including this item

    return matrix[n][m]
                
            

    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
 
 
    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result
