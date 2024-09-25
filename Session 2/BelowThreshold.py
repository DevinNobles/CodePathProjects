#Write a function count_less_than() that takes in a list of integers numbers and an integer threshold as parameters and returns the number of items in numbers that are less than threshold.

#Given
numbers = [12,8,2,4,4,10]


def countLessThan(nums, threshold):
    count = 0
    for x in nums:
        if x > threshold:
            count += 1
    print(count)


countLessThan(numbers, 5)