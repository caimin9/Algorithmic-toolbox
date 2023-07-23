# need to use the fact that the series of final digits in fibonacci numbers repeats in cycles of 60
import sys

def fibonacci_sum_naive(n):
    n = n % 60
    if n <= 1:
        return n

    previous = 0
    current  = 1
    my_sum   = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        my_sum = (my_sum + current) % 10

    return my_sum

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
