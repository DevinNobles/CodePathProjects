#Write a function doubled() that takes in a list of integers lst as a parameter and prints each item in the list multiplied by two.

#Given
list = [1,2,3]

def doubled(lst):
    i = 0
    for x in lst:
        lst[i] *= 2
        i +=1
    print(lst)

doubled(list)

