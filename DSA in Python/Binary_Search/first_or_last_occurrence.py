def firstAndLast(nums, target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(0, n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]


nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
print(firstAndLast(nums, 3))
