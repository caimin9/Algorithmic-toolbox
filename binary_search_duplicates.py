def binary_search(keys, query):
    #keys is our array
    #Query is the value we're looking for
    low = 0
    high = len(keys)-1
    result = -1

    
    while low <= high:
        mid = (high+low) //2
        guess = keys[mid]
#We have 3 conditions. 
#Our query is < guess, query == guess, query > guess
#If the query is < guess we look in the first half of the array
#If the query is > guess we look in the second half
#If the query is == to the guess we assign that value to the result and look in the first half of the array to see if there is any previous occurrences

            
        if query == guess:
            result = mid
            high = mid -1
            
        elif query < guess:
            high = mid -1 
                       
        else:   #query > guess:
            low = mid + 1
    
    return result

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
