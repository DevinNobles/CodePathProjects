#Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.

def findDivisors(n):
    for x in range(1, n+1):
        if n % x == 0:
            print(x)

findDivisors(100000)