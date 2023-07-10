def fib(x):
    lst = [0,1]
    if(x <= 1):
        return x
    for i in range(2,x+1):
        fib_number = lst[i-1] + lst[i-2]
        lst.append(fib_number)
    a =  str(lst[x])
    return a[-1]

x = int(input())
print(fib(x))
