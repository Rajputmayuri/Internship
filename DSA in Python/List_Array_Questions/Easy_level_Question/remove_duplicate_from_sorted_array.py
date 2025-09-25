"""Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique
element appears only once. The relative order of the
elements should be kept the same. Then return the
number of unique elements in nums."""

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
n = len(nums)
freq_map = {}
for i in range(0, n):
    freq_map[nums[i]] = 0
j = 0
for k in freq_map:
    nums[j] = k
    j += 1
print(j)
print(nums)

"""Time Complexity : O(2N) = O(N)
   Space Complexity : O(N)"""

"""Optimal Solution"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        return i + 1


sol = Solution()
print(sol.removeDuplicates([1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]))

"""Time Complexity : O(N)
   Space Complexity : O(1)"""
