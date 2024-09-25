#Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.

#given
list = [1,-2,-3,4]


def flip_sign(lst):
    for x in lst:
        x *= -1
    print(lst)


newList = flip_sign(list)
