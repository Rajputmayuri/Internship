"""Brute Force Solution"""


class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


sol = Solution()
nums = [5, 9, 1, 2, 4, 15, 6, 3]
print(sol.twoSum(nums, 13))

"""Time Complexity : O(N(N+1))/2 = O(N^2)
    Space Complexity :O(1)"""

"""Optimal solution"""


def twosum(nums, target):

    n = len(nums)
    hash_map = {}
    for i in range(0, n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]] = i


nums = [5, 9, 1, 2, 4, 15, 6, 3]
print(twosum(nums, 13))

"""Time Complexity : O(N)
    Space Complexity : O(N)"""
