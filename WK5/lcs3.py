#Uses python3

import sys

def lcs3(a, b, c):

    x = len(a)
    y = len(b)
    z = len(c)

    #Initialise matrix and fill with 0s
    #It's of dimensions x,y,z

    matrix = [[[0 for _ in range(z+1)] for _ in range(y+1)] for _ in range(x+1)]

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                
                if i == 0 or j==0 or k==0:
                    matrix[i][j][k] = 0
                #We move diagonally here if they're all the same
                elif a[i-1] == b[j-1] == c[k-1]:
                    matrix[i][j][k] = matrix[i-1][j-1][k-1] +1
                else: #Here we find the largest value to move to
                    matrix[i][j][k] = max(matrix[i][j][k-1],matrix[i][j-1][k],matrix[i-1][j][k])
    return matrix[x][y][z]            
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
