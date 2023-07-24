
import sys

def sort_key(x):
    return x * 3

def largest_number(a):
    # Convert numbers to strings
    a = list(map(str, a))
    # Sort numbers in descending order based on their string value
    a.sort(reverse=True, key=sort_key)
    # Combine the sorted numbers into a string
    largest_num = "".join(a)
    return largest_num

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

