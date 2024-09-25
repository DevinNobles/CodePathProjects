#Write a function print_indices() that takes in an integer list lst as a parameter and prints out the index of each item in the given list.
#Use the function range() to loop through the list indices.

list = [5,1,3,8,2]


def indices(lst):
    for x in lst:
        print(lst.index(x))

indices(list)