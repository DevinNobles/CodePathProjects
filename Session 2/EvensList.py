#Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.

#given
list = [1,2,3,4]

def getEvens(lst):
    even = []
    for x in lst:
        if x % 2 == 0:
            even.append(x)
    print(even)

getEvens(list)

            