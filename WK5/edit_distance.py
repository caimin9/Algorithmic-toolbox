# Uses python3
#mimnimising edit distance is the same as maximising alignment score
# s is string_1 and t is string_2
def edit_distance(s, t):
    n = len(s)
    m = len(t)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        d[i][0] = i

    for j in range(m+1):
        d[0][j] = j

    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = d[i][j-1] + 1
            deletion = d[i-1][j] + 1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1] + 1
            if s[i-1] != t[j-1]:
                d[i][j] = min(insertion, deletion, mismatch)
            else:
                d[i][j] = min(insertion, deletion, match)
    return d[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))


#pseudocode
'''
insertion = +1
deletion = +1
mismatch = +1

if a[i] == b[j] --> match
if a[i] != b[j] --> mismatch
# '''
# def ed(a,b):
#     d = float('inf') * (len(b)+1)
#     for i,j in d:
#         d[i,o] = i
#         d[0,j] = j
#     for j in range(1,m+1):
#         for i in range(1,n+1):
#             insertion = d[i,j-1] + 1
#             deletion = d[i-1,j] +1
#             match = d[i-1,j-1]
#             mismatch = d[i-1,j-1] +1
#             if a[i] == b[j]:
#                 d[i,j] = min(insertion,deletion,match)
#             else:
#                 d[i,j] = min(insertion,deletion,mismatch)
#     return d[n,m]
#     #n x m matrix
    #make optimal allignmnet by backtracking

    
# def outputAllignment(i,j):
#     if i==0 and j==0:
#         return
#     if i >0 and d[i,j] == d[i-1,j] +1:
#         outputAllignment(i-1,j)
        
#     elif j > 0 and d[i,j] == d[i,j-1] +1:
#         outputAllignment(i,j-1)
    
#     else:
#         outputAllignment(i-1,j-1):
            
        


