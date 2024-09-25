#Write a function linear_search() that takes in a list lst and value target as parameters. The function returns the index of target in lst if found. If target is not found in lst, return -1.

#given
list = [1,4,5,2,8]

def linear(lst, target):
    check = False
    for x in lst:
        if x == target:
            check = True
            position = lst.index(x)
            print(position)
    if(check == False):
        print(-1)

linear(list, 2)
