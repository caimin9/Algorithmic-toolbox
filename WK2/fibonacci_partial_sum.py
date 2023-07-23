def fibonacci_partial_sum_naive(from_, to):
    # Reduce the number by modulo 60, using the property of Pisano period
    from_, to = from_ % 60, to % 60

    # If 'to' is less than 'from_', it means 'to' has passed 60, we need to add 60 to make it larger
    if to < from_:
        to += 60

    _sum = 0
    current, _next = 0, 1

    # Loop until 'to'
    for i in range(to + 1):
        # Only sum the values where i is between 'from_' and 'to' (inclusive)
        if i >= from_:
            _sum += current

        # Apply modulo operation when summing the values to avoid large numbers
        _sum %= 10

        # Compute next Fibonacci number
        current, _next = _next, (current + _next) % 10

    return _sum

if __name__ == '__main__':
    import sys
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))

