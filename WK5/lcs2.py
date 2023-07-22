#Want to find the longest common subsequence between the two inputs
#Gonna n

import sys

def lcs2(a, b):
    '''
    Want to to initialise a matrix of size n+1 x m+1
     |a|b|c|d|
    a| | | | |
    d| | | | |
    b| | | | |
    c| | | | |
     | | | | |
     
    abcd and adbc are our inputs here
    if there's a match we go diagonally. And we add 1
    if there's no match we go to the right or down. We take the max of these two
    ''' 
    n = len(a)
    m = len(b)

    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    

    for i in range(1,n+1):
        for j in range(1,m+1):

            if i == 0 or j==0:
                matrix[i][j] = 0
            elif a[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1] +1
            else: #Here we take the larger of the values above or to the side
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    return matrix[n][m]
            

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
