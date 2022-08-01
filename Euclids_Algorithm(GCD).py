def GCD(a,b):
    if b== 0:
        return a
    a_prime = a % b
    return GCD(b,a_prime)
