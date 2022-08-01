def max_pairwise_product_two(numbers):
    lst = list()

    for number in numbers:
        lst.append(number)
    lst.sort()
    return (lst[-1] * lst[-2])


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_two(input_numbers))


from random import randint
def max_prod_stress(N,M):
    while True:
        n = randint(2,N)
        A = [None]*n
        for i in range(n):
            A[i] = randint(0,M)
        print(A)
        result1 = max_pairwise_product_two(A)
        result2 = max_pairwise_product_two(A)
        if result1==result2:
            print('OK')
        else:
            print('Wrong answer:',result1,result2)
            return
max_prod_stress(5,100)
