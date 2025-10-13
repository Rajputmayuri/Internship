"""Brute Force Solution"""

nums = [4, 5, 6, 7, 0, 1, 2]  # TC : O(N) and SC : O(1)
n = len(nums)
mini = float("inf")
for i in range(0, n):
    mini = min(mini, nums[i])
print(mini)

"""Optimal Solution"""
nums = [4, 5, 6, 7, 0, 1, 2]  # TC : O(logN) and SC : O(1)
n = len(nums)
low = 0
high = n - 1
mini = float("inf")
while low <= high:
    mid = (low + high) // 2
    if nums[mid] <= nums[high]:
        mini = min(mini, nums[mid])
        high = mid - 1
    else:
        mini = min(mini, nums[low])
        low = mid + 1
print(mini)
