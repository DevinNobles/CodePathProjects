import math

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
    


print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
print(is_prime(11))
print(is_prime(13))
