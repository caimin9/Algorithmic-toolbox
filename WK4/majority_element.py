'''
The goal is to implement a divide and conquer algo to see if we have a majority value in our array

'''
import sys
def get_majority_element(a, left, right):
    '''
    a is the array inputed that is not sorted
    left is 0
    right is length of array. (n or len(a))
    mid is the middle index of the array
    '''
    # Adjust right to be an index, not the length
    right -= 1

    if left == right:
        return a[left]

  #find the middle index to divide the array
    mid = (right - left) // 2 + left

    #Splitting the array into 2 sides and recursively calling the function
    low = get_majority_element(a, left, mid + 1)
    high = get_majority_element(a, mid + 1, right + 1)
    
    if low == high:
        return low
    
    #If left and right are not equal we need to count how many times each value occurs
    l_count = sum(1 for i in range(left, right + 1) if a[i] == low)
    r_count = sum(1 for i in range(left, right + 1) if a[i] == high)

    #Compare the 2 counts to find the element which occurs more
    #If either count occurs more than the other we know we have a majority element
    if l_count > (right - left + 1) // 2:
        return low
    elif r_count > (right - left + 1) // 2:
        return high
    else:
        return -1

    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)