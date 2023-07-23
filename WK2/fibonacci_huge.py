import sys


# Sequence of fib numbers modulo m are periodic
# Calculate this first to speed up the algo
# Pisano period used to reduce large fib numbers
def pisano_period_length(m):
    previous, current = 0, 1
    for i in range(0, m * 6):
        previous, current = current, (previous + current) % m
        if (previous, current) == (0, 1):
            return i + 1


def get_fibonacci_huge_naive(n, m):
    pisano_length = pisano_period_length(m)
    n = n % pisano_length

    if n <= 1:
        return n

    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

if __name__ == '__main__':
    import sys
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

