#Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.

#Given Input
list = [1,2,3]


newlst = []
def doublednew(lst):
    i = 0
    for x in lst:
        newlst.append(lst[i] * 2)
        i +=1
    print(newlst)

doublednew(list)
