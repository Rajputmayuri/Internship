"""Brute Force Solution"""


def search(nums, target):

    n = len(nums)  # TC : O(N)  & SC : O(1)
    for i in range(0, n):
        if nums[i] == target:
            return i
    return -1


nums = [11, 15, 20, 1, 4, 5, 6, 8, 9, 10]
print(search(nums, 8))


"""Optimal Solution"""


def search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:  # TC: O(LogN) & SC: O(1)
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


nums = [11, 15, 20, 1, 4, 5, 6, 8, 9, 10]
print(search(nums, 8))
