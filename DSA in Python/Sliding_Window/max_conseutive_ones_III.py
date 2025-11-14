"""Brute Force Solution"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        n = len(nums)
        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                if zeros <= k:
                    length = j - i + 1
                    max_length = max(max_length, length)
                else:
                    break
        return max_length


sol = Solution()
print(sol.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))

"""Optimal Solution"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        n = len(nums)
        zeros = 0
        max_length = 0
        while right < n:
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                max_length = max(max_length, length)
            right += 1

        return max_length


sol = Solution()
print(sol.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
