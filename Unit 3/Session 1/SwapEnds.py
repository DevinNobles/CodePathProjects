
def swap_ends(my_str):

    letters = []
    letters = list(my_str)
    L = letters[0]
    letters[0] = letters[-1]
    letters[-1] = L 
    print(letters)
    #code here
    pass


swap_ends('boat')
