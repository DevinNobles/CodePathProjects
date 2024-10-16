def sort_array_by_parity(nums):
    evens = []
    odds = []

    for i in nums:
        if i % 2 == 0:
           evens.append(i)
        else:
           odds.append(i)

    evens.extend(odds)
    return evens


numbs = [1,2,3,4,5,6,7,8,9,6,98,46,312,67,85,135,496]

print(sort_array_by_parity(numbs))
