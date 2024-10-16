def reverse_list(lst):
    front = 0
    back = len(lst) - 1

    while back > front:
        temp = lst[front]

        lst[front] = lst[back]
        lst[back]= temp

        front += 1
        back -= 1
    return lst

    
things = [1, 2, 3, 4, 5]

print(reverse_list(things))

