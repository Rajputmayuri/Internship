"""Brute Force Solution"""


def search(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return True
    return False


nums = [7, 7, 7, 7, 7, 7, 7, 1, 2, 3, 4, 5, 6, 7, 7]
print(search(nums, 10))

"""Optimal Solution"""


def search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1  # TC : O(LogN) SC : O(1)
            high -= 1
            continue
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return False


nums = [7, 7, 7, 7, 7, 7, 7, 1, 2, 3, 4, 5, 6, 7, 7]
print(search(nums, 7))
