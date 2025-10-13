"""Brute Force Solution"""


def numberOfOccurrence(nums, target):
    n = len(nums)
    count = 0
    for i in range(0, n):
        if nums[i] == target:
            count += 1

    return count


nums = [1, 1, 2, 2, 2, 2, 3, 2]
print(numberOfOccurrence(nums, 4))

"""Optimal Solution"""


class Solution:
    def lowerBound(self, arr, x: int) -> int:
        n = len(arr)
        lower_bound = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                lower_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        return lower_bound

    def upperBound(self, arr, x: int) -> int:
        n = len(arr)
        upper_bound = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > x:
                upper_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        return upper_bound

    def countFreq(self, arr, target):
        lb = self.lowerBound(arr, target)
        ub = self.upperBound(arr, target)

        # Check if target exists
        if lb == len(arr) or arr[lb] != target:
            return 0

        return ub - lb


arr = [5, 7, 7, 8, 8, 8, 8, 10]
target = 8
obj = Solution()
print(obj.countFreq(arr, target))

"""Time Complexity : O(2LogN) = O(LogN)
    Space Complexity : O(1)"""
