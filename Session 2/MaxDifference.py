#Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.

#given
list = [5,22,8,10,2]



def max_difference(lst):
    min = lst[1]
    max = lst[1]
    for x in lst:
        if x < min:
            min = x
        if x > max:
            max = x
    diff = max - min
    print(diff)


max_difference(list)