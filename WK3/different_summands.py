import sys

def optimal_summands(n):
    summands = []
    i = 1
    while n > 0:
        if n - i >= 0 and n - i > i:
            summands.append(i)
            n -= i
            i += 1
        else:
            summands.append(n)
            n = 0
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)

