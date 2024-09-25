def isSubsequence(lst, subsequence):
    for i in subsequence:
        found = False
        for j in lst:
            if i == j:
                found = True
                break
        if found == False:
            return False
    


    



list = [1, 3, 5, 6, 2, 7]
sub1 = [1, 3, 5]
sub2 = [1, 2, 3]
sub3 = [3, 6, 8, 0]
