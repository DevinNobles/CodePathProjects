#SUM OF STRINGS

def sum_of_number_strings(nums):
    total = 0

    for num in nums:
        total += int(num)

    return total

def remove_duplicates(nums):
    # current = 0
    # end = len(nums)

    # for x in range(1, end):
    #     if nums[current] == nums[x]:
    #           nums.pop(nums[x])
    #           end -= 1
    #     current +



    current = nums[0]
    end = len(nums)
    x = 0
    while x < end:
        
        if nums[x] == current:
            nums.pop(current)
            end = len(nums)
        else:
            current = nums[x]
        print(nums)
        x += 1    
        
    return print(nums)

nums = [1,1,1,2,3,4,4,5,6,6]
no_dups = [1,2,3,4,5,6]




remove_duplicates(nums)





