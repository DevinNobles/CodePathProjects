#Write a function that returns the sum of all the Elements in a list. 

# Complete the 'find_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY lst as parameter.
#

def find_sum(lst):
    sum = 0
    # Write your code here
    for num in lst:
        sum += num
    return sum 