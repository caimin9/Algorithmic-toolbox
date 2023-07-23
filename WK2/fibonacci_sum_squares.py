def fibonacci_sum_squares_naive(n):
    # Reduce n using the period length
    n = n % 60
    if n <= 1:
        return n

    # Calculate Fn and Fn+1
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    # Next number in sequence
    next_number = (previous + current) % 10

    # The sum of squares is Fn * Fn+1
    sum_squares = (current * next_number) % 10

    return sum_squares

if __name__ == '__main__':
    import sys
    n = int(sys.stdin.read())
    print(fibonacci_sum_squares_naive(n))
