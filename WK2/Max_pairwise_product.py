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
