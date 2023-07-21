# Uses python3
import sys
import random
#Want to sort the values of the array between l and r inclusive
def partition3(a, l, r):
    pivot = a[l]
    m = l  # Position where we place the next element less than or equal to pivot
    j = r
    i = l + 1
    while i <= j:
        if a[i] > pivot:
            a[i], a[j]= a[j], a[i]
            j -= 1
        elif a[i] == pivot:
            i += 1
        # For elements less than or equal to pivot, swap them to the left
        else: #a[i] < pivot:
            a[i], a[m] = a[m], a[i]
            m += 1
            i += 1
    return m

    
    #pass

# def partition2(a, l, r):
#     #x is the first element in the list
#     x = a[l] 
#     j = l   
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
