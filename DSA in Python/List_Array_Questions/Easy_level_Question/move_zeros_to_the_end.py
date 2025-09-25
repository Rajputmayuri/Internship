"""Brutforce Solution"""

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
n = len(nums)
temp = []
for i in range(0, n):
    if nums[i] != 0:
        temp.append(nums[i])
len_temp = len(temp)
for i in range(0, len_temp):
    nums[i] = temp[i]
for i in range(len_temp, n):
    nums[i] = 0
print(nums)

"""Time Complexity : O(N+N) = O(2N) = O(N)
   Space Complexity :O(N)"""

"""Optimal Solution"""

from typing import List


class Solution:
    def moveZeroes(self, nums):
        if len(nums) == 1:
            return
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        else:
            return
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1


sol = Solution()
nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
sol.moveZeroes(nums)
print(nums)
