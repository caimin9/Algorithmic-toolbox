#This returns the last digit of the sum of n fibonacci numbers

def fib(x):
    if x<= 1: return x
    a,b = 0,1
    sum = 1
    for i in range(x-1):
        a,b = b,a+b % 10
        sum += b
    val = str(sum)
    return val[-1]


x = int(input())
print(fib(x))
