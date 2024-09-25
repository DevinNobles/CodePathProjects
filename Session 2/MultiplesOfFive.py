#Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).

def mults():
    for x in range(1, 101):
        if x % 5 == 0:
            print(x)
        

mults()