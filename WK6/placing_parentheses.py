def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i,j,m,M,op):
    min_value = float('inf')
    max_value = float('-inf')
    for k in range(i,j):
        a = evalt(M[i][k],  M[k+1][j],op[k])
        b = evalt(M[i][k],  m[k+1][j],op[k])
        c = evalt(m[i][k],  M[k+1][j],op[k])
        d = evalt(m[i][k],  m[k+1][j],op[k])
        min_value = min(min_value,a,b,c,d)
        max_value = max(max_value,a,b,c,d)
    return min_value, max_value

def get_maximum_value(dataset):
    num = [int(i) for i in dataset[0::2]]
    op = [i for i in dataset[1::2]]

    n = len(num)
    m = [[0 for _ in range(n)] for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = num[i]
        M[i][i] = num[i]
    for s in range(1,n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i,j,m,M,op)
    
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
