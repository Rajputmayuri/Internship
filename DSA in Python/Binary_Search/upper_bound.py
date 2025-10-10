"""smallest index such that nums[i]>target"""

nums = [1, 1, 1, 2, 3, 4, 5, 6, 7, 7, 7, 9, 12, 12, 13]
n = len(nums)
target = 7
low = 0
high = n - 1
upper_bound = 15
while low <= high:
    mid = (low + high) // 2
    if nums[mid] > target:
        upper_bound = mid
        high = mid - 1
    else:
        low = mid + 1
print(upper_bound)
