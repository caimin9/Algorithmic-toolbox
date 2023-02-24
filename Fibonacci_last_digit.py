



def fib(x):
    if x<= 1: return x
    a,b = 0,1
    for i in range(x-1):
        a,b = b,(a+b % 10)
    val = str(a)
    return val[-1]


x = int(input())
print(fib(x))
