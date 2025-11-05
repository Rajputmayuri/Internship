from typing import List


class Solution:
    def solve(
        self, index: int, subset: List[int], nums: List[int], result: List[List[int]]
    ):
        # Base case: if we've considered all elements, store the current subset
        if index >= len(nums):
            result.append(subset.copy())
            return

        # Choice 1: Include the current element
        subset.append(nums[index])
        self.solve(index + 1, subset, nums, result)

        # Backtrack: remove the last element before exploring the next choice
        subset.pop()

        # Choice 2: Exclude the current element and move forward
        self.solve(index + 1, subset, nums, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(0, [], nums, result)
        return result


sol = Solution()
nums = [1, 2, 3]
all_subsets = sol.subsets(nums)
print(all_subsets)

"""Time Complexity : O(2^n)
    Space Complexity : O(n)"""
